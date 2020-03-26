from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def index2(request):
    return HttpResponse("Hello, Sanyam")

def index22(request):
    return HttpResponse("Hello, Sanyam Sanyam")