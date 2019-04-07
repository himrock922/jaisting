from django.test import TestCase, Client
from django.contrib.auth import get_user_model


class TemplateTest(TestCase):
    def test_login_require_jails(self):
        response = self.client.get('/jails/')
        self.assertRedirects(response, '/accounts/login/?next=/jails/')

    def test_login_require_jail_new(self):
        response = self.client.get('/jails/new')
        self.assertRedirects(response, '/accounts/login/?next=/jails/new')

    def test_access_jails(self):
        User = get_user_model()
        self.client = Client()
        self.client.force_login(User.objects.create_user('user'))
        response = self.client.get('/jails/')
        self.assertTemplateUsed(response, 'jails/index.html')
        self.client.logout()

    def test_access_jail_new(self):
        User = get_user_model()
        self.client = Client()
        self.client.force_login(User.objects.create_user('user'))
        response = self.client.get('/jails/new')
        self.assertTemplateUsed(response, 'jails/new.html')
        self.client.logout()
