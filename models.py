from operator import mod
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(default="")
    email = models.EmailField(default="")
    man = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)  #��ü�� ������ �� ������Ʈ ����
    
    def __str__(self):
        return self.title   # pk���� �����ϴ°� �ƴ� title���� �����ϰ� ����
