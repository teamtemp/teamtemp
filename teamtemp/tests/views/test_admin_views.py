__author__ = 'traviswarren'

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from teamtemp.responses.models import TeamTemperature


class AdminViewTestCases(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='user', email='test@email.com', password='password')

    def test_admin_redirects_if_not_authenticated(self):

        response = self.client.get(reverse('admin'))

        self.assertRedirects(response, 'http://testserver/accounts/login/?next=/admin/')

    def test_admin_get_creation(self):

        self.assertTrue(self.client.login(username=self.user.username, password='password'))

        response = self.client.get(reverse('admin'))

        self.assertTemplateUsed(response, 'admin.html')
        self.assertContains(response, 'Create a Team Temperature Survey', status_code=200)

    def test_admin_post_creation(self):

        self.assertTrue(self.client.login(username=self.user.username, password='password'))

        response = self.client.post(reverse('admin'))

        self.assertRedirects(response, 'http://testserver/admin/{}'
                             .format(TeamTemperature.objects.get(creator=self.user).id))