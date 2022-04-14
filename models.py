from operator import mod
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(default="")
    email = models.EmailField(default="")
    man = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)  #객체를 생성할 때 업데이트 해줌
    
    def __str__(self):
        return self.title   # pk값을 리턴하는게 아닌 title값을 리턴하게 해줌
