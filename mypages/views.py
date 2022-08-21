from django.shortcuts import render

# Create your views here.
def view_v(request):
    return render(request,'home.html')