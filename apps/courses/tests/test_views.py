from django.test import TestCase
from django.urls import reverse


class TestCoursesViews(TestCase):

    # TEST FOR COURSE_LIST VIEW

    # Test for course_list view. Response status code and template used.
    def test_course_list_status_code(self):
        response = self.client.get(reverse('course_list'))
        self.assertEqual(response.status_code, 200)

    # Test that the course_list view uses the correct template.
    def test_course_list_uses_correct_template(self):
        response = self.client.get(reverse('course_list'))
        self.assertTemplateUsed(response, 'courses/courses.html')

    # Test that the course_list view contains the expected context data.
    def test_course_list_context_contains_courses(self):
        response = self.client.get(reverse('course_list'))
        self.assertIn('courses', response.context)

    # Test that the course_list view context contains the expected
    # number of courses.
    def test_course_list_context_has_four_courses(self):
        response = self.client.get(reverse('course_list'))
        self.assertEqual(len(response.context['courses']), 4)

    # Test that the course_list view context contains the expected course
    # title for the first course.
    def test_course_list_first_course_title(self):
        response = self.client.get(reverse('course_list'))
        self.assertEqual(
            response.context['courses'][0]['course_title'],
            'Python: from fundamentals to details'
        )

    # TEST FOR COURSE_DETAIL VIEW

    # Test for course_detail view. Response status code,
    # template used, and context data.
    def test_course_detail_status_code(self):
        response = self.client.get(reverse('course_detail'))
        self.assertEqual(response.status_code, 200)

    # Test that the course_detail view uses the correct template.
    def test_course_detail_uses_correct_template(self):
        response = self.client.get(reverse('course_detail'))
        self.assertTemplateUsed(response, 'courses/course_detail.html')

    # Test that the course_detail view contains
    # the expected context data.
    def test_course_detail_context_contains_course(self):
        response = self.client.get(reverse('course_detail'))
        self.assertIn('course', response.context)

    # Test that the course_detail view context contains the expected course
    # title.
    def test_course_detail_title_is_correct(self):
        response = self.client.get(reverse('course_detail'))
        self.assertEqual(
            response.context['course']['course_title'],
            'Python: from fundamentals to details'
        )

    # Test that the course_detail view context contains the expected number of
    # course content sections.
    def test_course_detail_has_three_course_content_sections(self):
        response = self.client.get(reverse('course_detail'))
        self.assertEqual(len(response.context['course']['course_content']), 3)

    # Test that the course_detail view context contains
    # the expected instructor name.
    def test_course_detail_instructor_is_correct(self):
        response = self.client.get(reverse('course_detail'))
        self.assertEqual(
            response.context['course']['info_course']['instructor'],
            'Alison Walsh'
        )

    # Test that the course_detail view context contains
    # the expected total number of
    # lessons.
    def test_course_detail_total_lessons_info_is_correct(self):
        response = self.client.get(reverse('course_detail'))
        self.assertEqual(
            response.context['course']['info_course']['lessons'],
            59
        )

    # Test that the course_detail view context contains
    # the expected course link.
    def test_course_detail_course_link_is_correct(self):
        response = self.client.get(reverse('course_detail'))
        self.assertEqual(
            response.context['course']['course_link'],
            'course_lessons'
        )

    # TEST FOR COURSE_LESSONS VIEW

    # Test for course_lessons view. Response status code,
    # template used, and context data.
    def test_course_lessons_status_code(self):
        response = self.client.get(reverse('course_lessons'))
        self.assertEqual(response.status_code, 200)

    # Test that the course_lessons view uses the correct template.
    def test_course_lessons_uses_correct_template(self):
        response = self.client.get(reverse('course_lessons'))
        self.assertTemplateUsed(response, 'courses/course_lessons.html')

    # Test that the course_lessons view contains
    # the expected context data.
    def test_course_lessons_context_contains_lesson(self):
        response = self.client.get(reverse('course_lessons'))
        self.assertIn('lesson', response.context)

    # Test that the course_lessons view context contains
    # the expected course title.
    def test_course_lessons_title_is_correct(self):
        response = self.client.get(reverse('course_lessons'))
        self.assertEqual(
            response.context['lesson']['course_title'],
            'Python: from fundamentals to details'
        )

    # Test that the course_lessons view context contains
    # the expected course progress.
    def test_course_lessons_progress_is_correct(self):
        response = self.client.get(reverse('course_lessons'))
        self.assertEqual(
            response.context['lesson']['course_progress'],
            30
        )

    # Test that the course_lessons view context contains
    def test_course_lessons_has_three_sections(self):
        response = self.client.get(reverse('course_lessons'))
        self.assertEqual(
            len(response.context['lesson']['course_content']),
            3
        )

    # Test that the course_lessons view context contains
    # the expected total number of lessons for the first section.
    def test_course_lessons_first_section_total_lessons_is_correct(self):
        response = self.client.get(reverse('course_lessons'))
        self.assertEqual(
            response.context['lesson']['course_content'][0]['total_lessons'],
            2
        )

    # Test that the course_lessons view context contains
    # the expected number of completed lessons for the second section.
    def test_course_lessons_second_section_completed_lessons_is_correct(self):
        response = self.client.get(reverse('course_lessons'))
        self.assertEqual(
            response.context['lesson']['course_content'][1]['completed_lessons'],
            1
        )

    # Test that the course_lessons view context contains
    # the expected name for the third lesson in the first section.
    def test_course_lessons_third_section_name_is_correct(self):
        response = self.client.get(reverse('course_lessons'))
        self.assertEqual(
            response.context['lesson']['course_content'][2]['name'],
            'Control Structures'
        )
