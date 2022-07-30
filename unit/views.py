from typing import Optional
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from accounts.models import Teacher
from unit.models import Faculty, Lecture


# Create your views here.

class UnitView(LoginRequiredMixin, TemplateView):

    template_name = 'unit/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["faculties"] = Faculty.objects.all()
        context["title"] = "Unit"
        return context

class FacultyCreationView(LoginRequiredMixin, CreateView):

    template_name: str = 'unit/faculty/create.html'
    model = Faculty
    success_url: Optional[str] = reverse_lazy('unit:indexPage') 
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teachers"] = Teacher.objects.all()
        context["lectures"] = Lecture.objects.all()
        return context

    def form_valid(self, form):
        messages.success(self.request, "Faculté créee avec success.") 
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.success(self.request, "Echec creation d'une nouvelle faculte.") 
        return super().form_valid(form)

class LectureCreationView(LoginRequiredMixin, CreateView):
    model = Lecture
    fields = '__all__'

    def form_valid(self, form):
        messages.success(self.request, "Cours ajouté avec success.") 
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "Echec creation du cours") 
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return HttpResponseRedirect(self.request.path_info)
