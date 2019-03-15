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
    

class Student(models.Model):
    studentID  = models.IntegerField(primary_key=True, verbose_name="학생코드")	
    name = models.CharField(max_length=50, verbose_name="이름")	
    major = models.ForeignKey(Major, on_delete=models.CASCADE, verbose_name="전공") # Major의 primary_key 와 매칭
    phone =  models.CharField(max_length=50, blank=True, verbose_name="전화번호")
    address = models.CharField(max_length=50, verbose_name="주소", blank=True)	
    hobby =	models.CharField(max_length=50, verbose_name="취미", blank=True)
    skill = models.CharField(max_length=50, verbose_name="보유기술", blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('course:s_list')