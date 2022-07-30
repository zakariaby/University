from django.contrib.messages.api import success
from django.urls import path
import accounts.views as a_views
from django.contrib.auth.views import LogoutView, PasswordChangeView

from django.conf import settings
from django.conf.urls.static import static

from django.urls import reverse_lazy

app_name = 'accounts'

urlpatterns = [

    # Accounts Routers
    path('login/', a_views.AppLoginView.as_view(), name='loginPage'),
    path('register/', a_views.AppRegisterView.as_view(), name='registerPage'),
    path('logout/', a_views.applogout, name='logoutPage'),
    # Student routes
    path('student/add/', a_views.StudentCreationView.as_view(), name="createStudentPage"),
    path('student/detail/<int:pk>/', a_views.StudentDetailView.as_view(), name="detailStudentPage"),
    
    # Teacher routes
    path('teacher/add/', a_views.TeacherCreationView.as_view(), name="createTeacherPage"),

    # Password Routers
    # path('mot_de_passe/modifier/<int:pk>/', a_views.change_password_view, name='passwordChangePage'),
    # path('mot_de_passe/modifier_admin/<int:pk>/', PasswordChangeView.as_view(success_url=reverse_lazy('accounts:profilePage'), template_name='dashboard/users/password_admin_change.html'), name='passwordAdminChangePage'),
    # Exporting Excel Files
    # path('export/produit/', a_views.export_product_view, name='exportProductView'),
    # path('export/vente/', a_views.export_vente_view, name='exportVenteView'),
    # path('export/client/', a_views.export_client_view, name='exportClientView'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
