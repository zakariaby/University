from typing import Optional
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .models import Enrollment
from accounts.models import Student


# Create your views here.

class EnrollmentView(LoginRequiredMixin, TemplateView):

    template_name = 'enrollment/index.html'
    # form_class = VenteFormSingle
    # success_url = reverse_lazy('ventes:ventePage')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["enrollments"] = Enrollment.objects.all()
        context["title"] = "Enrollment"
        return context


class EnrollmentCreateView(LoginRequiredMixin, CreateView):

    template_name: str = "enrollment/create.html"
    model = Enrollment
    fields = "__all__"
    success_url: Optional[str] = reverse_lazy("enrollment:indexPage")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["students"] = Student.objects.all()
        return context

    def form_valid(self, form):
        messages.success(self.request, "{} {} inscript avec succes.".format(
            form.instance.student.first_name, form.instance.student.last_name))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "Echec de l'inscription")
        return super().form_valid(form)
