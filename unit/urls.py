from django.urls import path
import unit.views as v_views

app_name = 'unit'

urlpatterns = [
    # Vente Routers
    path('', v_views.UnitView.as_view(), name="indexPage"),

    # path('supprimer_plusieur/', v_views.multiple_delete_vente, name='multipleDeleteVentePage'),
    # path('detail/<int:pk>/<int:day>/', v_views.vente_detail, name='venteDetailPage'),
]
