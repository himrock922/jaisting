from django.test import TestCase

class JailsViewTest(TestCase):
    def test_login_require_jails(self):
        response = self.client.get('/jails/')
        self.assertRedirects(response, '/accounts/login/?next=/jails/')