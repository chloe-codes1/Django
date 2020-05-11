from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('json1/', views.article_list_json_1),
    path('json2/', views.article_list_json_2),
    path('json3/', views.article_list_json_3),
]