from django.db import models

# Create your models here.

from django.conf import settings
from django.utils import timezone

# models.CharField – 文字数が制限されたテキストを定義するフィールド
# models.TextField – 制限無しの長いテキスト用
# models.DateTimeField – 日付と時間のフィールド
# models.ForeignKey – これは他のモデルへのリンク

class Post(models.Model): #Postというオブジェクトを定義
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title