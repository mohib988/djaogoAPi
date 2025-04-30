from django.contrib import admin
from django.urls import path, include
from promptApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
     
    path('',views.CustomPromptView.as_view() ),
    path("login/", views.login_view, name="login"),   
]
urlpatterns += static(settings.STATIC_URL+settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)