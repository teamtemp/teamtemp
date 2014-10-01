__author__ = 'traviswarren'

from django.test import TestCase
from django.core.urlresolvers import reverse

from teamtemp.tests.factories import TeamTemperatureFactory


class TemperatureViewTestCases(TestCase):
    def test_get_temperature_view(self):

        team_temp = TeamTemperatureFactory()

        response = self.client.get(reverse('temp', args=[str(team_temp.id)]))

        self.assertTemplateUsed(response, 'form.html')
        self.assertContains(response, 'Submit your temperature')

    def test_post_invalid_temperature_view(self):

        team_temp = TeamTemperatureFactory()

        response = self.client.post(reverse('temp', args=[str(team_temp.id)]),
                                            data={'score': 2})

        self.assertTemplateUsed(response, 'form.html')
        # self.failIf(response.context_data['form'].is_valid())
        self.assertFormError(response, 'form', 'word', 'This field is required.')

    def test_post_valid_temperature_view(self):

        team_temp = TeamTemperatureFactory()

        response = self.client.post(reverse('temp', args=[str(team_temp.id)]),
                                            data={'score': 2, 'word': 'word'})

        self.assertTemplateUsed(response, 'form.html')
        self.assertContains(response, "Thank you for submitting your answers. "
                                      "You can amend them now or later if you need to")
