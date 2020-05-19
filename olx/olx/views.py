from django.shortcuts import render

def home(request):
    return render(request, 'registration/home.html')

def about(request):
    return render(request,'registration/about.html')

def contact(request):
    return render(request,'registration/contact.html')    