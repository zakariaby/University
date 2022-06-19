from django.urls import path
import dashboard.views as d_views


app_name = 'dashboard'

urlpatterns = [

    # This is the home page
    path('', d_views.IndexView.as_view(), name="homePage"),

]
