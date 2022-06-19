from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .models import Enrollment



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
