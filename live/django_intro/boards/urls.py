from django.urls import path
from . import views

urlpatterns = [
    # /boards/
    path('', views.index),
    path('new/', views.new),
    path('complete/', views.complete),
    ]