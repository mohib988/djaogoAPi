from django.contrib import admin
from django.urls import path, include
from promptApp import views

urlpatterns = [
     
    path('',views.CustomPromptView.as_view() ),

    
]