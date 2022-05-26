"""Define URL patterns for blogs"""
from django.urls import re_path

from . import views

app_name = 'blogs'
urlpatterns = [ 
    #Home page
    re_path(r'^$', views.index, name='index'),
    #Page to post new blog
    re_path(r'^new_post/$', views.new_post, name='new_post'),
    #Page to edit existing blog
    re_path(r'^edit_blog/(?P<post_id>\d+)/$', views.edit_post, name='edit_post'),
]