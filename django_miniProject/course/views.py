from django.shortcuts import render
from . models import Major
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
# Create your views here.

major_list = ListView.as_view(model=Major)
