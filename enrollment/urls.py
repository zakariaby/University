from django.urls import path
import enrollment.views as enrol_views

app_name = 'enrollment'

urlpatterns = [
    # Vente Routers
    path('', enrol_views.EnrollmentView.as_view(), name="indexPage"),

    # path('supprimer_plusieur/', v_views.multiple_delete_vente, name='multipleDeleteVentePage'),
    # path('detail/<int:pk>/<int:day>/', v_views.vente_detail, name='venteDetailPage'),
]
