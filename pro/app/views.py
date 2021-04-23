from django.shortcuts import render
from django.views.generic import CreateView , UpdateView ,DeleteView,ListView
from django import views
from .models import Student
from django.urls import reverse_lazy
from .forms import sud

class Create_Student(CreateView,ListView):
    form_class=sud
    queryset=Student.objects.all()
    template_name='Student.html'
    success_url=reverse_lazy('Student') 

