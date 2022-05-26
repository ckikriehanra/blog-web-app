"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, include

urlpatterns = [
    re_path(r'admin/', admin.site.urls),
    #before add this path we need to specify app_name in urls.py in blogs folder 
    re_path(r'', include('blogs.urls', namespace='blogs')),
    #add app_url for users app
    re_path(r'', include('users.urls', namespace='users')),
]
