from django.shortcuts import redirect, render, reverse
from . models import Major, Student
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
# Create your views here.

major_list = ListView.as_view(model=Major, template_name="course/major_list.html")
major_detail = DetailView.as_view(model=Major, template_name="course/major_detail.html")
major_edit = UpdateView.as_view(model=Major, fields="__all__", template_name="course/major_form.html")
major_delete = DeleteView.as_view(model=Major, template_name="course/major_confirm_delete.html", success_url='/course/major/') #success_url 필수
major_new = CreateView.as_view(model=Major, fields="__all__", template_name="course/major_form.html")

student_list = ListView.as_view(model=Student, template_name="course/student_list.html")
student_detail = DetailView.as_view(model=Student, template_name="course/student_detail.html")
student_edit = UpdateView.as_view(model=Student, fields="__all__", template_name="course/student_form.html")
student_delete = DeleteView.as_view(model=Student, template_name="course/student_confirm_delete.html", success_url='/course/student/')
student_new = CreateView.as_view(model=Student, fields="__all__", template_name="course/student_form.html")

# index page
def index(request):
     return render(request, 'course/index.html')

# 데이터 관리 페이지
def manageData(request):
     return render(request, 'course/data.html')

# 전체 데이터 삭제
import pymysql
def deleteData(request):
    # MySQL Connection 연결
    conn = pymysql.connect(host = 'localhost', 
                       user = 'root', 
                       password = '1234',
                       db = 'course', 
                       charset='utf8')
    
    # Connection 으로부터 Cursor 생성
    curs = conn.cursor()
    
    # SQL문 실행
    sql = "delete from course_student"
    curs.execute(sql)    
    sql = "delete from course_major"
    curs.execute(sql)

    # 변경사항 db 반영 
    conn.commit()
    
    # Connection 닫기
    conn.close()

    return render(request, 'course/data.html')               


# Ajax
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from django.http import HttpResponse

@csrf_exempt # 403 error 제어
def searchMajor(request):
    m_title = request.POST["m_title"] # 전공아이디로 검색
    major = Major.objects.filter( major_title__contains = m_title)

    return render(request, 'course/major_list2.html', {'major_list':major})

@csrf_exempt
def searchStd(request):
    m_title = request.POST["m_title"]
    if m_title == "전체학생":
        student = Student.objects.all
        return render(request, 'course/student_list2.html', {'student_list':student})
    else:    
        student = Student.objects.filter( major__major_title__contains = m_title)

        return render(request, 'course/student_list2.html', {'student_list':student})