from django.urls import path
from . import views

urlpatterns = [
    # /articles/
    path('', views.index),
    path('new/', views.new),
    path('create/',views.create),
    path('<int:pk>/',views.detail),
]