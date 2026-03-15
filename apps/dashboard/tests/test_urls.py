from django.test import SimpleTestCase
from django.urls import reverse, resolve
from apps.dashboard import views


class TestDashboardUrls(SimpleTestCase):
    def test_dashboard_url_is_resolved(self):
        url = reverse('dashboard')
        self.assertEqual(resolve(url).func, views.index)
