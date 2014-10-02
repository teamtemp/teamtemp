import re

from django import forms
from django.forms.util import ErrorList
from teamtemp.responses.models import TemperatureResponse, TeamTemperature
from django.utils.safestring import mark_safe
from django.utils.html import escape


class TeamTemperatureForm(forms.ModelForm):
    class Meta:
        model = TeamTemperature
        fields = []


class ErrorBox(ErrorList):
    def __unicode__(self):
        return mark_safe(self.as_box())

    def as_box(self):
        if not self: return u''
        return u'<div class="error box">%s</div>' % self.as_lines()

    def as_lines(self):
        return "<br/>".join(e for e in self)


class SurveyResponseForm(forms.ModelForm):
    class Meta:
        model = TemperatureResponse
        fields = ['score', 'word']