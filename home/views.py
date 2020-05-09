from django.shortcuts import render, HttpResponse

# Create your views here.
def home(index):
    return HttpResponse('home')
def contact(index):
    return HttpResponse('contact blog')
def about(index):
    return HttpResponse('about blog')