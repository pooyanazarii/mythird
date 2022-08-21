from django.contrib import admin
from django.urls import path
from mypages.views import *
app_name="mypages"
urlpatterns = [
    path('',view_index,name='index'),
    path('about',view_about,name='about'),
    path('class',view_class,name='class'),
    path('contact',view_contact,name='contact'),
    path('gallery',view_gallery,name='gallery'),
    path('single',view_single,name='single'),
    path('team',view_team,name='team'),
]
