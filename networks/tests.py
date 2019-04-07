from django.test import TestCase


class NetworksViewTest(TestCase):
    def test_login_require_networks_new(self):
        response = self.client.get('/networks/new')
        self.assertRedirects(response, '/accounts/login/?next=/networks/new')
