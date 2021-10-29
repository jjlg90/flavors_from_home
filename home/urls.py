from django.contrib import admin
from django.urls import path
from . import views
from .views import contact, success

urlpatterns = [
    path('', views.index, name='home'),
    path("contact", views.contact, name="contact"),
    path('success/', views.success, name='success'),
]
