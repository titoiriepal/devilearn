from django.test import SimpleTestCase
from django.urls import reverse, resolve
from apps.profiles import views


class TestProfilesUrls(SimpleTestCase):

    def test_profile_url_is_resolved(self):
        url = reverse('profile')
        self.assertEqual(resolve(url).func, views.index)
