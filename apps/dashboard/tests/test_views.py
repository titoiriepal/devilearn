from django.test import TestCase
from django.urls import reverse


# TEST FOR INDEX VIEW

class TestDashboardIndexView(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('dashboard'))

    # Test for index view. Response status code,
    # template used, and context data.
    def test_status_code_is_200(self):
        self.assertEqual(self.response.status_code, 200)

    # Test that the index view uses the correct template.
    def test_uses_correct_template(self):
        self.assertTemplateUsed(self.response, 'dashboard/index.html')

    # Test that the index view contains the welcome message.
    def test_page_contains_welcome_message(self):
        self.assertContains(self.response, 'Welcome, Ricardo!')

    # Test that the index view contains the second card name.
    def test_page_contains_second_card_name(self):
        self.assertContains(self.response, 'Courses')
