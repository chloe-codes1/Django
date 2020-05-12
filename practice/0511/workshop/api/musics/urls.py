from django.urls import path
from . import views

# drf_yasg 사용하기
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# 설정
schema_view = get_schema_view(
   openapi.Info(
      title="Music API",
      default_version='v1',
      description="Music/Artist/Comment API Server",
    #   terms_of_service="https://www.google.com/policies/terms/",
    #   contact=openapi.Contact(email="contact@snippets.local"),
    #   license=openapi.License(name="BSD License"),
   ),
)

urlpatterns = [
    path('artists/', views.artist_list_create),
    path('artists/<int:artist_pk>/', views.artist_detail_update_delete),
    path('musics/', views.music_list_create),
    path('musics/<int:music_pk>/', views.music_detail_update_delete),
    path('musics/<int:music_pk>/comments/', views.comment_create),
    path('comments/<int:comment_pk>/', views.comment_update_delete),
    path('swagger/', schema_view.with_ui('swagger')),
    path('redoc', schema_view.with_ui('redoc')),
]