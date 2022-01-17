from django.http import HttpResponseRedirect, JsonResponse,HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from datetime import datetime
from django.core import serializers

import requests
import random 

from django.views.generic import ListView, DetailView, CreateView

from .models import Schools, Classes, Courses, Questions ,Answers,MyAnswers
from .forms import SchoolsForm, ClassesForm, CoursesForm, QuestionsForm, AnswersForm, MyAnswersForm


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
    def get_queryset(self):
        classes = Classes.objects.all()
        
    def get_context_data(self, **kwargs):
        context = super(ClassesIndexView, self).get_context_data(**kwargs)
        classes = Classes.objects.all()
        newClassObj = []
        for classroom in classes:
            schools = Schools.objects.filter(schools_id=classroom.schools_id)
            newClassObj.append({"schoolsList":schools,"class":classroom})   
        context['classes_list'] = newClassObj
        return context
  
  
class CoursesIndexView(ListView):
    template_name = 'education/courses_index.html'

    def get_queryset(self):
        return Courses.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CoursesIndexView, self).get_context_data(**kwargs)
        courses = Courses.objects.all()
        newClassObj = []
        for course in courses:
            schools = Schools.objects.filter(schools_id=course.schools_id)
            classes = Classes.objects.filter(schools_id=course.classes_id)
            newClassObj.append({"schoolsList":schools,"classList":classes,"courses":course})   
        context['courses_list'] = newClassObj
        return context    


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

 
def courses_edit(request, pk, template_name='education/courses_edit.html'):
    courses = get_object_or_404(Courses, pk=pk)
    form = CoursesForm(request.POST or None, instance=courses)
    if form.is_valid():
        form.instance.userId = request.user.id
        form.save()
        return redirect('education:courses_index')
    return render(request, template_name, {'form':form})
  
  
class CoursesDetailsView(DetailView):
    model = Courses
    template_name = 'education/courses_details.html'

    def get_context_data(self, **kwargs):
        context = super(CoursesDetailsView, self).get_context_data(**kwargs)
        context['question_datails'] = Questions.objects.filter(courses_id=self.kwargs.get('pk'))
        return context


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
    
    
def set_user_type(request):
    request.session["name"] = request.POST['accessType']
    request.session["test_session"] = random.randint(2345678909800, 9923456789000)           
    return redirect('education:index')
      
    
    
    
 # Questions section
class QuestionsIndexView(ListView):
    template_name = 'education/questions_index.html'
    context_object_name = 'questions_list'

    def get_queryset(self):
        return Questions.objects.all()


class QuestionsCreateView(CreateView):
    model = Questions
    form_class = QuestionsForm
    template_name = 'education/questions_create.html'
    def get_success_url(self):
        return reverse_lazy('education:courses_details', kwargs={'pk': self.kwargs['courses_id']})

    def form_valid(self, form):
        form.instance.userId = self.request.user.id
        form.instance.pub_date = datetime.now()        
        form.instance.courses_id = self.kwargs['courses_id']
        return super().form_valid(form)

  
class QuestionsDetailsView(DetailView):
    model = Questions
    template_name = 'education/questions_details.html'

    def get_context_data(self, **kwargs):
        context = super(QuestionsDetailsView, self).get_context_data(**kwargs)
        context['answers_datails'] = Answers.objects.filter(questions_id=self.kwargs.get('pk'))
        return context



def questions_edit(request, pk, template_name='education/questions_edit.html'):
    questions = get_object_or_404(Questions, pk=pk)
    form = QuestionsForm(request.POST or None, instance=questions)
    if form.is_valid():
        form.instance.userId = request.user.id
        form.save()
        return redirect(reverse_lazy('education:courses_details', kwargs={'pk': questions.courses_id}))
    return render(request, template_name, {'form':form})
    


def questions_Correct_answer(request, pk, template_name='education/questions_correctanswer.html'):
    questions = get_object_or_404(Questions, pk=pk)
    obj = Questions.objects.get(id=questions.id)
    obj.correct_answer = request.POST["correct_answer"]
    obj.save()
    return redirect(reverse_lazy('education:questions_details', kwargs={'pk': questions.id}))    


def questions_delete(request, pk, template_name='education/questions_confirm_delete.html'):
    questions = get_object_or_404(Questions, pk=pk)
    if request.method=='POST':
        questions.delete()
        return redirect(reverse_lazy('education:courses_details', kwargs={'pk': questions.courses_id}))
    return render(request, template_name, {'object':questions})
 
  
     
    
    
 # Answers section
class AnswersIndexView(ListView):
    template_name = 'education/answers_index.html'
    context_object_name = 'answers_list'

    def get_queryset(self):
        return Answers.objects.all()


class AnswersCreateView(CreateView):
    model = Answers
    form_class = AnswersForm
    template_name = 'education/answers_create.html'
    def get_success_url(self):
        return reverse_lazy('education:questions_details', kwargs={'pk': self.kwargs['questions_id']})

    def form_valid(self, form):
        form.instance.userId = self.request.user.id
        form.instance.pub_date = datetime.now()        
        form.instance.questions_id = self.kwargs['questions_id']
        return super().form_valid(form)



def answers_edit(request, pk, template_name='education/answers_edit.html'):
    answers = get_object_or_404(Answers, pk=pk)
    form = AnswersForm(request.POST or None, instance=answers)
    if form.is_valid():
        form.instance.userId = request.user.id
        form.save()
        return redirect(reverse_lazy('education:questions_details', kwargs={'pk': answers.questions_id}))
    return render(request, template_name, {'form':form})
    


def answers_delete(request, pk, template_name='education/answers_confirm_delete.html'):
    answers = get_object_or_404(Answers, pk=pk)
    if request.method=='POST':
        answers.delete()
        return redirect(reverse_lazy('education:questions_details', kwargs={'pk': answers.questions_id}))
    return render(request, template_name, {'object':answers})
 
  
  
  
  #Get Exams settings
      
def get_schools(request):
    if request.is_ajax and request.method == "GET":
        school_query = "SELECT * from education_schools "
        schools = Schools.objects.raw(school_query)

        context = {}
        schools_data = serializers.serialize('json', schools)
        return JsonResponse({'schools_data': schools_data})
    return JsonResponse(data={'error':'error'})
      
      
def get_classes(request, pk):
    schools = get_object_or_404(Schools, pk=pk)
    
    if request.is_ajax and request.method == "GET":
        classes = Classes.objects.filter(schools_id=schools.schools_id);
        context = {}
        classes_data = serializers.serialize('json', classes)
        return JsonResponse({'classes_data': classes_data})
    return JsonResponse(data={'error':'error'})
          
      
def get_courses(request, classes_pk, schools_pk):
    schools = get_object_or_404(Schools, pk=schools_pk)
    classes = get_object_or_404(Classes, pk=classes_pk)
    
    if request.is_ajax and request.method == "GET":
        courses = Courses.objects.filter(classes_id=classes.id, schools_id=schools.schools_id);
        context = {}
        courses_data = serializers.serialize('json', courses)
        return JsonResponse({'courses_data': courses_data})
    return JsonResponse(data={'error':'error'})         
      
    
class MyExamsView(ListView):
    template_name = 'education/my_exams.html'
    context_object_name = 'questions_list'

    def get_queryset(self):
        if not self.request.session['test_session']:
            self.request.session["test_session"] = random.randint(2345678909800, 9923456789000)
            
        return Questions.objects.filter(courses_id=self.kwargs.get('courses_pk'))

    def get_context_data(self, **kwargs):      
        context = super(ListView,self).get_context_data(**kwargs)
        context['courses'] = Courses.objects.filter(id=self.kwargs.get('courses_pk'))
        return context
        

 
def get_answers(request, questions_pk):
    questions = get_object_or_404(Questions, pk=questions_pk)
    
    if request.is_ajax and request.method == "GET":
        if request.session.get("finished"):
            return JsonResponse(data={'error':'error'})          
        else:
            answers = Answers.objects.filter(questions_id=questions.id);
            context = {}
            answers_data = serializers.serialize('json', answers)
            return JsonResponse({'answers_data': answers_data})
    else:    
        return JsonResponse(data={'error':'error'})          

 

def save_answers(request):
    if request.method == 'POST':
        form = MyAnswersForm(request.POST)
        
        if form.is_valid():
            form.instance.answers_id = request.POST['answers_id']
            form.instance.questions_id = request.POST['questions_id']
            form.instance.test_session = request.session['test_session']
            form.instance.userId = request.user.id
            form.instance.pub_date = datetime.now()
            updated_rows = MyAnswers.objects.filter(test_session=request.session['test_session'],questions_id=request.POST['questions_id'])
            if not updated_rows:
                form.save()
                return HttpResponse("success")
            else:
                MyAnswers.objects.filter(test_session=request.session['test_session'],questions_id=request.POST['questions_id']).update(answers_id=request.POST['answers_id'])          
                return HttpResponse("Already exist")
        else:
            errors = form.errors
            return HttpResponse(simplejson.dumps(errors))  
    else:
        return HttpResponse("error")   
    


def finish_answers(request, schools_id,classes_id,courses_id,session_id, template_name='education/finish.html'):
    schools = get_object_or_404(Schools, pk=schools_id)
    if request.method=='GET':
        request.session["finished"] = "true";
        courses = Courses.objects.filter(id=courses_id)
        questions = Questions.objects.filter(courses_id=courses_id)
        myanswers = MyAnswers.objects.filter(test_session=session_id)
        
        newObj = []
        correctAnswers = 0
        wrongAnswers = 0
        for question in questions:
            count = 1
            isCorrect = "false"

            for myanswer in myanswers:
                if int(question.correct_answer) == int(myanswer.answers_id):
                    newObj.append({"question":question.questions_name, "status":"Correct"})
                    isCorrect = "true"
                    correctAnswers+=1
                else:
                    if int(question.correct_answer) != int(myanswer.answers_id) and int(count) == len(myanswers) and isCorrect=="false":
                        newObj.append({"question":question.questions_name, "status":"Wrong"})
                        wrongAnswers+=1
                count+=1
              
        scoretotal = 0            
        score = (correctAnswers/len(questions))*100
        if score > 0:
            scoretotal = score
        
        
        context = {}           
        context['score'] = int(scoretotal)
        context['newObj'] = newObj
        context['questions'] = questions
        context['myanswers'] = myanswers
        context['courses'] = courses
        return render(request, template_name, {'context':context})
    return render(request, template_name, {'object':schools})



def print_certificate(request, schools_id,classes_id,courses_id,session_id,fullname, template_name='education/print_certificate.html'):
    schools = get_object_or_404(Schools, pk=schools_id)
    if request.method=='GET':
        courses = Courses.objects.filter(id=courses_id)
        questions = Questions.objects.filter(courses_id=courses_id)
        myanswers = MyAnswers.objects.filter(test_session=session_id)
        
        newObj = []
        correctAnswers = 0
        wrongAnswers = 0
        for question in questions:
            count = 1
            isCorrect = "false"

            for myanswer in myanswers:
                if int(question.correct_answer) == int(myanswer.answers_id):
                    newObj.append({"question":question.questions_name, "status":"Correct"})
                    isCorrect = "true"
                    correctAnswers+=1
                else:
                    if int(question.correct_answer) != int(myanswer.answers_id) and int(count) == len(myanswers) and isCorrect=="false":
                        newObj.append({"question":question.questions_name, "status":"Wrong"})
                        wrongAnswers+=1
                count+=1
              
        scoretotal = 0            
        score = (correctAnswers/len(questions))*100
        if score > 0:
            scoretotal = score
        
        
        context = {}           
        context['score'] = int(scoretotal)
        context['name'] = fullname
        context['newObj'] = newObj
        context['questions'] = questions
        context['myanswers'] = myanswers
        context['courses'] = courses
        context['schools'] = schools
        return render(request, template_name, {'context':context})
    return render(request, template_name, {'object':schools})