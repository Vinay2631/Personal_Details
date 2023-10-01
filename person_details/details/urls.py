from django.urls import path
from django.contrib.auth import views as auth_views
from details import views
from .views import DetailsmCreateView


urlpatterns = [
    path('home/',views.home,name='home'),
    path('update/details/',DetailsmCreateView.as_view(),name='detailsm-create'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/',views.register, name='register'),
]