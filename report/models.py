from django.db import models

# 作成日時、更新日時fieldを定義したモデル
# このモデルを継承することで2つのfieldの定義を省略することができる
from model_utils.models import TimeStampedModel
from accounts.models import CustomUser

class Post(TimeStampedModel):
    # created = models.DateTimeField(auto_now_add=True)　新規作成
    # modified = models.DateTimeField(auto_now=True) 更新
    created = models.DateTimeField() # オーバーライド
    title = models.CharField(max_length=255)
    body = models.TextField()
    user_name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title