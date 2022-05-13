from django.contrib import admin

# Register your models here.

from .models import Post
#Postモデルを登録
admin.site.register(Post)