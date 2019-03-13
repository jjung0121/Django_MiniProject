from django.urls import path, re_path
from django.conf.urls import url
from . import views

app_name = "course"

urlpatterns = [
    path('', views.major_list, name = "m_list"), # 전공 전체 조회
    path('<pk>/detail/', views.major_detail, name = "m_detail"), # 전공 상세 조회
    path('<pk>/edit/', views.major_edit, name = "m_edit"), # 전공 수정
    path('<pk>/delete/', views.major_delete, name = "m_delete"), # 전공 삭제
    path('new/', views.major_new, name = "m_new"), # 전공 신규 등록
]
