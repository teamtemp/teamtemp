__author__ = 'traviswarren'

from datetime import datetime

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from responses.models import TeamTemperature

from teamtemp import utils


class TempViewTestCases(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='user', email='test@email.com', password='password')

    # def test_temp_redirects_if_not_authenticated(self):
    #
    #     temp = TeamTemperature.objects.get_or_create(id=utils.random_string(8),
    #                                                  creation_date=datetime.now(), creator=self.user)
    #
    #     # think this view could move to a Class based view using kwargs and uuid's to clean up testing
    #     response = self.client.get(temp[0].id)
    #
    #     self.assertRedirects(response, 'http://testserver')