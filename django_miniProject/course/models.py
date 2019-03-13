from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Major(models.Model):
    major_id = models.IntegerField(primary_key=True, verbose_name="전공코드")
    major_title = models.CharField(max_length=50, verbose_name="전공명")

    def __str__(self): # admin page 및 customer에게 노출되는 값
        return self.major_title

    def get_absolute_url(self): #생성 / 수정 / 삭제 작업 후, return page
        return reverse('course:m_list')
    