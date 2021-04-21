from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),

    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
    path('profile/', views.profile, name='profile'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('update_profile/', views.update_profile, name='update_profile'),

    # Client - Server configuration
    path('client/', views.client, name='client'),
    path('server/', views.server, name='server'),
    path('terminal/', views.terminal, name='terminal'),

    # Main Menu - Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
]
