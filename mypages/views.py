from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view_v(request):
    return HttpResponse("this test in application")