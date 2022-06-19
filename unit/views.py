from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic.edit import CreateView
from django.views.generic import TemplateView


# Create your views here.

class UnitView(LoginRequiredMixin, TemplateView):

    template_name = 'unit/index.html'
    # form_class = VenteFormSingle
    # success_url = reverse_lazy('ventes:ventePage')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Unit"
        return context
