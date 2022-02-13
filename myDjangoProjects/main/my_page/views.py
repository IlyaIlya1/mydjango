from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def home(request):
    return render(request, "my_page/home.html")

def uslugi(request):
    return render(request, "my_page/uslugi.html")

def contacts(request):
    return render(request, "my_page/contacts.html")


