from typing import Optional
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from unit.models import Faculty


# Create your views here.

class UnitView(LoginRequiredMixin, TemplateView):

    template_name = 'unit/index.html'
    # form_class = VenteFormSingle
    # success_url = reverse_lazy('ventes:ventePage')

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

    def form_valid(self, form):
        messages.success(self.request, "Faculté créee avec success.") 
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "Echec creation d'une nouvelle faculte.") 
        return super().form_valid(form)
