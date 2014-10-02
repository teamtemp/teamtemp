from datetime import datetime

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, DetailView

from teamtemp.responses.mixins import CreatorRequiredMixin
from teamtemp.responses.forms import SurveyResponseForm, ErrorBox, TeamTemperatureForm
from teamtemp.responses.models import User, TeamTemperature, TemperatureResponse
from teamtemp import responses


class CreateTeamTemperatureView(CreateView):
    form_class = TeamTemperatureForm
    template_name = 'admin.html'

    def get_success_url(self):
        return reverse('result', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.creation_date = datetime.now()
        return super(CreateTeamTemperatureView, self).form_valid(form)


class TeamTemperatureDetailView(CreatorRequiredMixin, DetailView):
    model = TeamTemperature
    template_name = 'results.html'
    context_object_name = 'survey'


def submit(request, survey_id):
    userid = responses.get_or_create_userid(request)
    user, created = User.objects.get_or_create(id=userid)
    survey = get_object_or_404(TeamTemperature, pk=survey_id)
    thanks = ""
    if request.method == 'POST':
        form = SurveyResponseForm(request.POST, error_class=ErrorBox)
        response_id = request.POST.get('id', None)
        if form.is_valid():
            srf = form.cleaned_data
            # TODO check that id is unique!
            response = TemperatureResponse(id=response_id, request=survey, score=srf['score'], word=srf['word'], responder=user)
            response.save()
            response_id = response.id
            form = SurveyResponseForm(instance=response)
            thanks = "Thank you for submitting your answers. You can " \
                     "amend them now or later if you need to"
    else:
        try:
            previous = TemperatureResponse.objects.get(request=survey_id, responder=user)
            response_id = previous.id
        except TemperatureResponse.DoesNotExist:
            previous = None
            response_id = None

        form = SurveyResponseForm(instance=previous)
    return render(request, 'form.html', {'form': form, 'thanks': thanks, 'response_id': response_id})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            login(request, new_user)
            return HttpResponseRedirect("/admin/")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {'form': form, })

