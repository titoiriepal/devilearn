from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView
from django.urls import reverse, reverse_lazy

from ..models import Course


class InstructorRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_instructor


class CourseListView(InstructorRequiredMixin, ListView):
    model = Course
    template_name = 'instructor/course_list.html'
    context_object_name = 'courses'
    paginate_by = 8

    def get_queryset(self):
        return Course.objects.filter(owner=self.request.user)


class CourseCreateView(InstructorRequiredMixin, CreateView):
    model = Course
    # We specify the fields we want to show in the course creation form
    # Cargamos los campos que queremos mostrar
    # en el formulario de creación de curso
    fields = ['title', 'slug', 'overview', 'image',
              'level', 'duration', 'categories']
    template_name = 'instructor/course_form.html'
    # After creating a new course, we redirect
    # to the instructor's course list
    # Redirigimos a la lista de cursos del instructor
    # después de crear un nuevo curso
    success_url = reverse_lazy('instructor:course_list')

    def form_valid(self, form):
        # We set the owner of the course to the current user
        # before saving the form
        # Establecemos el propietario del curso como el usuario actual
        # antes de guardar el formulario
        form.instance.owner = self.request.user
        return super().form_valid(form)
