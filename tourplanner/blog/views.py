from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    return HttpResponse("<h1>Blog Under Construction </h1>")