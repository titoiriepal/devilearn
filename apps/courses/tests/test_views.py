from django.test import TestCase
from django.urls import reverse


# TEST FOR COURSE_LIST VIEW
class TestCoursesListView(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('course_list'))

    # Test for course_list view. Response status code,
    # template used, and context data.
    def test_status_code_is_200(self):
        self.assertEqual(self.response.status_code, 200)

    # Test that the course_list view uses the correct template.
    def test_course_list_uses_correct_template(self):
        self.assertTemplateUsed(self.response, 'courses/courses.html')

    # Test that the course_list view contains the expected context data.
    def test_context_contains_courses(self):
        self.assertIn('courses', self.response.context)

    # Test that the course_list view context contains the expected
    # number of courses.
    def test_context_has_four_courses(self):
        self.assertEqual(len(self.response.context['courses']), 4)

    # Test that the course_list view context contains the expected course
    # title for the first course.
    def test_first_course_title_is_correct(self):
        self.assertEqual(
            self.response.context['courses'][0]['course_title'],
            'Python: from fundamentals to details'
        )

    # TEST FOR COURSE_DETAIL VIEW


class TestCourseDetailView(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('course_detail'))

    # Test for course_detail view. Response status code,
    # template used, and context data.
    def test_status_code_is_200(self):
        self.assertEqual(self.response.status_code, 200)

    # Test that the course_detail view uses the correct template.
    def test_uses_correct_template(self):
        self.assertTemplateUsed(self.response, 'courses/course_detail.html')

    # Test that the course_detail view contains
    # the expected context data.
    def test_context_contains_course(self):
        self.assertIn('course', self.response.context)

    # Test that the course_detail view context contains the expected course
    # title.
    def test_title_is_correct(self):
        self.assertEqual(
            self.response.context['course']['course_title'],
            'Python: from fundamentals to details'
        )

    # Test that the course_detail view context contains the expected number of
    # course content sections.
    def test_has_three_course_content_sections(self):
        self.assertEqual(
            len(self.response.context['course']['course_content']), 3)

    # Test that the course_detail view context contains
    # the expected instructor name.
    def test_course_detail_instructor_is_correct(self):
        self.assertEqual(
            self.response.context['course']['info_course']['instructor'],
            'Alison Walsh'
        )

    # Test that the course_detail view context contains
    # the expected total number of
    # lessons.
    def test_total_lessons_info_is_correct(self):
        self.assertEqual(
            self.response.context['course']['info_course']['lessons'],
            59
        )

    # Test that the course_detail view context contains
    # the expected course link.
    def test_course_link_is_correct(self):
        self.assertEqual(
            self.response.context['course']['course_link'],
            'course_lessons'
        )

    # TEST FOR COURSE_LESSONS VIEW


class TestCourseLessonsView(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('course_lessons'))

    # Test for course_lessons view. Response status code,
    # template used, and context data.
    def test_status_code_is_200(self):
        self.assertEqual(self.response.status_code, 200)

    # Test that the course_lessons view uses the correct template.
    def test_uses_correct_template(self):
        self.assertTemplateUsed(self.response, 'courses/course_lessons.html')

    # Test that the course_lessons view contains
    # the expected context data.
    def test_context_contains_lesson(self):
        self.assertIn('lesson', self.response.context)

    # Test that the course_lessons view context contains
    # the expected course title.
    def test_title_is_correct(self):
        self.assertEqual(
            self.response.context['lesson']['course_title'],
            'Python: from fundamentals to details'
        )

    # Test that the course_lessons view context contains
    # the expected course progress.
    def test_progress_is_correct(self):
        self.assertEqual(
            self.response.context['lesson']['course_progress'],
            30
        )

    # Test that the course_lessons view context contains
    # the expected number of course content sections.

    def test_has_three_sections(self):
        self.assertEqual(
            len(self.response.context['lesson']['course_content']),
            3
        )

    # Test that the course_lessons view context contains
    # the expected total number of lessons for the first section.
    def test_first_section_total_lessons_is_correct(self):
        self.assertEqual(
            self.response.context['lesson']['course_content'][0]['total_lessons'],
            2
        )

    # Test that the course_lessons view context contains
    # the expected number of completed lessons for the second section.
    def test_second_section_completed_lessons_is_correct(self):
        self.assertEqual(
            self.response.context['lesson']['course_content'][1]['completed_lessons'],
            1
        )

    # Test that the course_lessons view context contains
    # the expected name for the third lesson in the first section.
    def test_third_section_name_is_correct(self):
        self.assertEqual(
            self.response.context['lesson']['course_content'][2]['name'],
            'Control Structures'
        )
