from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime

from django.views.generic import ListView, DetailView

from .models import Schools, Classes, Courses
from .forms import SchoolsForm, ClassesForm, CoursesForm


class IndexView(ListView):
    template_name = 'education/index.html'

    def get_queryset(self):
        return Schools.objects.all()

        
class SchoolsIndexView(ListView):
    template_name = 'education/schools_index.html'
    context_object_name = 'schools_list'

    def get_queryset(self):
        return Schools.objects.all()

        
class ClassesIndexView(ListView):
    template_name = 'education/class_index.html'
    context_object_name = 'classes_list'

    def get_queryset(self):
        return Classes.objects.all()
  
  
class CoursesIndexView(ListView):
    template_name = 'education/courses_index.html'
    context_object_name = 'courses_list'

    def get_queryset(self):
        return Courses.objects.all()


def schools_create(request):
    if request.method == 'POST':
        form = SchoolsForm(request.POST)
        if form.is_valid():
            form.instance.userId = request.user.id
            form.instance.pub_date = datetime.now()      
            form.save()
            return redirect('education:schools_index')
    form = SchoolsForm()

    return render(request,'education/schools_create.html',{'form': form})
 
 
def class_create(request):
    if request.method == 'POST':
        form = ClassesForm(request.POST)
        if form.is_valid():
            form.instance.userId = request.user.id
            form.instance.pub_date = datetime.now()      
            form.save()
            return redirect('education:class_index')
    form = ClassesForm()

    return render(request,'education/class_create.html',{'form': form})
 
 
def courses_create(request):
    if request.method == 'POST':
        form = CoursesForm(request.POST)
        if form.is_valid():
            form.instance.userId = request.user.id
            form.instance.pub_date = datetime.now()      
            form.save()
            return redirect('education:courses_index')
    form = CoursesForm()

    return render(request,'education/courses_create.html',{'form': form})


def schools_edit(request, pk, template_name='education/schools_edit.html'):
    school = get_object_or_404(Schools, pk=pk)
    form = SchoolsForm(request.POST or None, instance=school)
    if form.is_valid():
        form.instance.userId = request.user.id
        form.save()
        return redirect('education:schools_index')
    return render(request, template_name, {'form':form})
  
  
def class_edit(request, pk, template_name='education/class_edit.html'):
    classes = get_object_or_404(Classes, pk=pk)
    form = ClassesForm(request.POST or None, instance=classes)
    if form.is_valid():
        form.instance.userId = request.user.id
        form.save()
        return redirect('education:class_index')
    return render(request, template_name, {'form':form})
 
 
def courses_edit(request, pk, template_name='education/courses_edit.html'):
    courses = get_object_or_404(Courses, pk=pk)
    form = CoursesForm(request.POST or None, instance=courses)
    if form.is_valid():
        form.instance.userId = request.user.id
        form.save()
        return redirect('education:courses_index')
    return render(request, template_name, {'form':form})


def schools_delete(request, pk, template_name='education/schools_confirm_delete.html'):
    school = get_object_or_404(Schools, pk=pk)
    if request.method=='POST':
        school.delete()
        return redirect('education:schools_index')
    return render(request, template_name, {'object':school})
 
 
def class_delete(request, pk, template_name='education/class_confirm_delete.html'):
    classes = get_object_or_404(Classes, pk=pk)
    if request.method=='POST':
        classes.delete()
        return redirect('education:class_index')
    return render(request, template_name, {'object':classes})
  
  
def courses_delete(request, pk, template_name='education/courses_confirm_delete.html'):
    courses = get_object_or_404(Courses, pk=pk)
    if request.method=='POST':
        courses.delete()
        return redirect('education:courses_index')
    return render(request, template_name, {'object':courses})