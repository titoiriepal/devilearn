from django.shortcuts import render

# Create your views here.


def course_list(request):
    courses = [
        {
            'id': 1,
            'course_title': 'Python: from fundamentals to details',
            'instructor': 'Alison Walsh',
            'description': '''
            Three-month Course to Learn the Basics of Python and Start Coding.
            ''',
            'rating': 4.5,
            'level': 'Beginner',
            'course_image': 'images/curso_1.jpg',
            'instructor_image': '''
            https://randomuser.me/api/portraits/women/68.jpg
            '''
        },
        {
            'id': 2,
            'course_title': 'Create strong web apps',
            'instructor': 'Patty Kutch',
            'description': '''
            Guide to Successful Company Management: Business And More
            ''',
            'rating': 4.7,
            'level': 'Beginner',
            'course_image': 'images/curso_2.jpg',
            'instructor_image': '''
            https://randomuser.me/api/portraits/women/20.jpg
            '''
        },
        {
            'id': 3,
            'course_title': 'Advanced Django',
            'instructor': 'Alonzo Murray',
            'description': '''
            A Fascinating Theory of Probability. Application. How to Outplay...
            ''',
            'rating': 4.8,
            'level': 'Advanced',
            'course_image': 'images/curso_3.jpg',
            'instructor_image': '''
            https://randomuser.me/api/portraits/men/32.jpg
            '''
        },
        {
            'id': 4,
            'course_title': 'Advanced FastAPI',
            'instructor': 'Gregory Harris',
            'description': '''
            Machine Learning and LLM. Implementation in Modern Software
            ''',
            'rating': 5.0,
            'level': 'Advanced',
            'course_image': 'images/curso_4.jpg',
            'instructor_image': '''
            https://randomuser.me/api/portraits/men/45.jpg
            '''
        },
    ]
    return render(request, 'courses/courses.html', {
        'courses': courses,
    })


def course_detail(request):
    course = {
        'id': 1,
        'course_title': 'Python: from fundamentals to details',
        'course_link': 'course_lessons',
        'info_course': {
            'lessons': 59,
            'duration': 8,
            'instructor': 'Alison Walsh',
        },
        'course_content': [
            {
                'id': 1,
                'name': 'Introduction to Python',
                'lessons': [
                    {
                        'name': 'What is Python?',
                        'type': 'video',
                    },
                    {
                        'name': 'How to use the web?',
                        'type': 'article',
                    },
                ],
            },
            {
                'id': 2,
                'name': 'Data Types and Variables',
                'lessons': [
                    {
                        'name': 'Data Types in Python',
                        'type': 'video',
                    },
                    {
                        'name': 'variables and Assignments',
                        'type': 'video',
                    },
                    {
                        'name': 'strings and Numbers',
                        'type': 'video',
                    },
                ],
            },
            {
                'id': 3,
                'name': 'Control Structures',
                'lessons': [
                    {
                        'name': 'if statements',
                        'type': 'video',
                    },
                    {
                        'name': 'for and while loops',
                        'type': 'video',
                    },
                    {
                        'name': 'switch statements',
                        'type': 'video',
                    },
                    {
                        'name': 'referenced links',
                        'type': 'article',
                    },
                ],
            },
        ],
        'description': '''
        Three-month Course to Learn the Basics of Python and Start Coding.
        ''',
        'rating': 4.5,
        'level': 'Beginner',
        'course_image': 'images/curso_1.jpg',
        'instructor_image': 'https://randomuser.me/api/portraits/women/15.jpg',
    }
    return render(request, 'courses/course_detail.html', {
        'course': course,
    })


def course_lessons(request):
    lesson = {
        'id': 1,
        'course_title': 'Python: from fundamentals to details',
        'course_progress': 30,
        'course_content': [
            {
                'id': 1,
                'name': 'Introduction to Python',
                'total_lessons': 2,
                'completed_lessons': 2,
                'lessons': [
                    {
                        'name': 'What is Python?',
                        'type': 'video',
                    },
                    {
                        'name': 'How to use the web?',
                        'type': 'article',
                    },
                ],
            },
            {
                'id': 2,
                'name': 'Data Types and Variables',
                'total_lessons': 3,
                'completed_lessons': 1,
                'lessons': [
                    {
                        'name': 'Data Types in Python',
                        'type': 'video',
                    },
                    {
                        'name': 'variables and Assignments',
                        'type': 'video',
                    },
                    {
                        'name': 'strings and Numbers',
                        'type': 'video',
                    },
                ],
            },
            {
                'id': 3,
                'name': 'Control Structures',
                'total_lessons': 4,
                'completed_lessons': 0,
                'lessons': [
                    {
                        'name': 'if statements',
                        'type': 'video',
                    },
                    {
                        'name': 'for and while loops',
                        'type': 'video',
                    },
                    {
                        'name': 'switch statements',
                        'type': 'video',
                    },
                    {
                        'name': 'referenced links',
                        'type': 'article',
                    },
                ],
            },
        ],
        'description': '''
        Three-month Course to Learn the Basics of Python and Start Coding.
        ''',
    }
    return render(request, 'courses/course_lessons.html', {
        'lesson': lesson,
    })
