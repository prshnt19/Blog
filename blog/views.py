from django.shortcuts import render, HttpResponse

# Create your views here.
def bloghome(index):
    return HttpResponse('bloghome')
def blogPost(request,slug):
    return HttpResponse(f'blog :{slug}')