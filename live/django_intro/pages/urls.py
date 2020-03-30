from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('hello/', views.hello),
    path('lotto/', views.lotto),
    path('cube/<int:num>/', views.cube),
    path('about_me/',views.about_me),
    path('lunch/', views.lunch),
    #variable routing
    path('hi/<str:name>/', views.hi),
    path('add/<int:a>/<int:b>', views.add),
    path('dinner/<str:menu>/<int:num>/', views.dinner),
    path('posts/<int:id>/', views.posts),
    ]