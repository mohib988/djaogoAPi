from django.contrib import admin
from django.urls import path, include
from promptApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve


urlpatterns = [
     
    path('',views.CustomPromptView.as_view() ),
    path("login/", views.login_view, name="login"),   

]
