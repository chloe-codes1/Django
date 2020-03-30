"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
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
