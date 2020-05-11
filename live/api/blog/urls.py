from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.article_list), # blog/api/v1/articles/
    path('<int:article_pk>/', views.article_detail), # blog/api/v1/articles/100
    path('create/', views.create_article), # blog/api/v1/articles/create/
]