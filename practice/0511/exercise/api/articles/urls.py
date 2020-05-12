from django.urls import path
from .import views

# drf_yasg 사용하기
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# 설정
schema_view = get_schema_view(
   openapi.Info(
      title="Articless API",
      default_version='v1',
      description="Board API Server",
    #   terms_of_service="https://www.google.com/policies/terms/",
    #   contact=openapi.Contact(email="contact@snippets.local"),
    #   license=openapi.License(name="BSD License"),
   ),
)

"""
[개발자를 위한 URL]

/api/v1/
C: POST /articles/
R: GET /articles/
R: GET /articles/<id>
U: PUT /articles/<id>
D: DELETE /articles/<id>
"""

app_name='articles'

urlpatterns = [
    path('articles/', views.article_list_create),
    path('articles/<int:article_pk>/', views.article_detail_update_delete),
    path('comments/', views.comment_list),
    path('swagger/', schema_view.with_ui('swagger')),
    path('redocs/', schema_view.with_ui('redoc')),
]

