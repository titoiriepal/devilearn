from django.test import SimpleTestCase
from django.urls import reverse, resolve
from apps.courses import views


class TestCoursesUrls(SimpleTestCase):
    def test_courses_url_is_resolved(self):
        url = reverse('course_list')
        self.assertEqual(resolve(url).func, views.course_list)

    def test_course_detail_url_is_resolved(self):
        url = reverse('course_detail')
        self.assertEqual(resolve(url).func, views.course_detail)

    def test_course_lessons_url_is_resolved(self):
        url = reverse('course_lessons')
        self.assertEqual(resolve(url).func, views.course_lessons)
