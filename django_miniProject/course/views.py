from django.shortcuts import render
from . models import Major
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
# Create your views here.

major_list = ListView.as_view(model=Major, template_name="course/major_list.html")
major_detail = DetailView.as_view(model=Major, template_name="course/major_detail.html")
major_edit = UpdateView.as_view(model=Major, fields="__all__", template_name="course/major_form.html")
major_delete = DeleteView.as_view(model=Major, template_name="course/major_confirm_delete.html", success_url='/course/') #success_url 필수
major_new = CreateView.as_view(model=Major, fields="__all__", template_name="course/major_form.html")


# Ajax
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from django.http import HttpResponse

@csrf_exempt
def searchMajor(request):
    m_id = request.POST["m_id"] # 전공아이디로 검색
    major = Major.objects.filter( major_title__contains = m_id)

    return render(request, 'course/major_list2.html', {'major_list':major})
    