from django.shortcuts import render
from . models import Major
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
# Create your views here.

major_list = ListView.as_view(model=Major, template_name="course/major_list.html")
major_detail = DetailView.as_view(model=Major, template_name="course/major_detail.html")
major_edit = UpdateView.as_view(model=Major, fields="__all__", template_name="course/major_form.html")
major_delete = DeleteView.as_view(model=Major, template_name="course/major_confirm_delete.html", success_url='/course/') #success_url 필수
major_new = CreateView.as_view(model=Major, fields="__all__", template_name="course/major_form.html")
