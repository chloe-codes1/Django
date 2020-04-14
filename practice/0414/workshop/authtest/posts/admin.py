from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at', )

# 어드민 사이트에 등록해줘
admin.site.register(Post, PostAdmin)