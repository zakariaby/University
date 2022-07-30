from django.urls import path
import unit.views as v_views

app_name = 'unit'

urlpatterns = [
    # Vente Routers
    path('', v_views.UnitView.as_view(), name="indexPage"),
    path('faculty/add/', v_views.FacultyCreationView.as_view(), name="facultyCreationPage"),
    path('lecture/add/', v_views.LectureCreationView.as_view(), name="lectureCreationPage"),
]
