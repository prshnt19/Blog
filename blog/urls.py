from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('post_comment',views.comment,name='post_comment'),
    path('',views.bloghome,name='bloghome'),
    path('<str:slug>',views.blogPost,name='blogPost'),
    

]
