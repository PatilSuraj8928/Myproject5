from django.shortcuts import render
from django.http import HttpResponse

def first(request):
    return HttpResponse('<h1>Good Morning</h>')

def second(request):
    return HttpResponse('<center>I hope you are doing well!</center>')