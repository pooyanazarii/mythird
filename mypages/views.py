from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def view_index(request):
    return render(request,'mypages/index.html')
def view_about(request):
    return render(request,'mypages/about.html')

def view_class(request):
    return render(request,'mypages/class.html')
    
def view_contact(request):
    return render(request,'mypages/contact.html')
    
def view_gallery(request):
    return render(request,'mypages/gallery.html')
    
def view_single(request):
    return render(request,'mypages/single.html')
    
def view_team(request):
    return render(request,'mypages/team.html')
