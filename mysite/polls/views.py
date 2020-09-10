from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello world. we are at the polls index.")

def detail(request):
    return HttpResponse("hello world. we are at the polls detail")

def vote(request):
    return HttpResponse("hello world. we are at the polls vote")

def result(request):
    return HttpResponse("hello world. we are at the polls result")
