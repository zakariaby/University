from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from accounts.models import Student, Teacher
from unit.models import Faculty
from enrollment.models import Enrollment

# Create your views here.


class IndexView(LoginRequiredMixin, TemplateView):

    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["students"] = Student.objects.all().order_by("created_at")
        context["teachers"] = Teacher.objects.all().order_by("created_at")
        context["faculties"] = Faculty.objects.all().order_by("created_at")
        context["enrollments"] = Enrollment.objects.all().order_by("created_at")
        return context
