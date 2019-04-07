from django.test import TestCase, Client
from django.contrib.auth import get_user_model


class TopViewTest(TestCase):
    def test_login_require_jails(self):
        User = get_user_model()
        self.client = Client()
        self.client.force_login(User.objects.create_user('user'))
        response = self.client.get('/jails/')
        self.assertTemplateUsed(response, 'jails/index.html')
