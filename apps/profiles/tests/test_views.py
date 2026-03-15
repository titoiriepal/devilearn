from django.test import TestCase
from django.urls import reverse


# TEST FOR INDEX VIEW

class TestProfilesIndexView(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('profile'))

    # Test for index view. Response status code,
    # template used, and context data.
    def test_status_code_is_200(self):
        self.assertEqual(self.response.status_code, 200)

    # Test that the index view uses the correct template.
    def test_uses_correct_template(self):
        self.assertTemplateUsed(self.response, 'profiles/profile.html')

    # Test that the index view contains the form title.
    def test_page_contains_form_title(self):
        self.assertContains(self.response, 'Edit Profile')

    # Test that the index view contains the email label.
    def test_page_contains_email_label(self):
        self.assertContains(self.response, 'Email')

    # Test that the index view contains the username label.
    def test_page_contains_name_label(self):
        self.assertContains(self.response, 'Name')

    # Test that the index view contains the last name label.
    def test_page_contains_last_name_label(self):
        self.assertContains(self.response, 'Last Name')

    # Test that the index view contains the company label.
    def test_page_contains_company_label(self):
        self.assertContains(self.response, 'Company')

    # Test that the index view contains the profession label.
    def test_page_contains_professional_title_label(self):
        self.assertContains(self.response, 'Professional Title')

    # Test that the index view contains the time_zone label.
    def test_page_contains_time_zone_label(self):
        self.assertContains(self.response, 'Time Zone')

    # Test that the index view contains the save changes button.
    def test_page_contains_save_changes_button(self):
        self.assertContains(self.response, 'Save Changes')
