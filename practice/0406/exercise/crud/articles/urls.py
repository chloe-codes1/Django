from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:pk>/', views.details),
    path('<int:pk>/edit/',views.update),
    path('<int:pk>/detail/',views.details),
    path('<int:pk>/delete/', views.delete),
    path('<int:pk>/update/', views.update),
    path('search/',views.search),
]
