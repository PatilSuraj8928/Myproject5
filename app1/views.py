from django.shortcuts import render
from django.http import HttpResponse

def first(request):
    return HttpResponse('<h1>Hey Hi there!!</h1>')

def second(request):
    return HttpResponse('<h2>This is Suraj</h2>')