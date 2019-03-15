from django.urls import path, re_path
from django.conf.urls import url
from . import views

app_name = "course"

urlpatterns = [
    path('major/', views.major_list, name = "m_list"), # 전공 전체 조회
    path('major/<pk>/detail/', views.major_detail, name = "m_detail"), # 전공 상세 조회
    path('major/<pk>/edit/', views.major_edit, name = "m_edit"), # 전공 수정
    path('major/<pk>/delete/', views.major_delete, name = "m_delete"), # 전공 삭제
    path('major/new/', views.major_new, name = "m_new"), # 전공 신규 등록
    path('major/searchMajor/', views.searchMajor, name = "m_search"), # 전공 조회 

    path('student/', views.student_list, name = "s_list"), # 학생 전체 조회
    path('student<pk>/detail/', views.student_detail, name = "s_detail"), # 학생 상세 조회
    path('student/<pk>/edit/', views.student_edit, name = "s_edit"), # 전공 수정
    path('student/<pk>/delete/', views.student_delete, name = "s_delete"), # 학생 삭제
    path('student/new/', views.student_new, name = "s_new"), # 학생 조회

]
