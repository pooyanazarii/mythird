from django.contrib import admin
from django.urls import path
from mypages.views import *

urlpatterns = [
    path('view_v',view_v),

]
