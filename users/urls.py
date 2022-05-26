""""Define URL for users app"""
from django.urls import include, re_path
from django.contrib.auth.views import LoginView 

from . import views

app_name = 'users'
urlpatterns = [ 
    #Page to login
    re_path(r'^login/$', LoginView.as_view(template_name = 'users/login.html'),
            name='login'),
    #Page to logout
    re_path(r'^logout/$', views.logout_view, name='logout'),
    #Page to redister
    re_path(r'^register/$', views.register, name='register'),
]