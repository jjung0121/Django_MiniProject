from django.db import models

# Create your models here.

class Major(models.Model):
    major_id = models.CharField(max_length=50)
    major_title = models.CharField(max_length=50)

    def __str__(self): # admin page에서 노출되는 값
        return self.major_title