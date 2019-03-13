from django.db import models

# Create your models here.

class Major(models.Model):
    major_id = models.IntegerField(primary_key=True, verbose_name="전공코드")
    major_title = models.CharField(max_length=50, verbose_name="전공명")

    def __str__(self): # admin page에서 노출되는 값
        return self.major_title