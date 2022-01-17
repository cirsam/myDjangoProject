from django import forms
from .models import Schools, Classes, Courses, Questions, Answers, MyAnswers

class SchoolsForm(forms.ModelForm):
    class Meta:
        model = Schools
        fields = "__all__"
        

class ClassesForm(forms.ModelForm):
    class Meta:
        model = Classes
        fields = "__all__"
        labels = {
            'schools_id': 'Schools',
            'class_name':'Class Name'
        }
        school = forms.ModelChoiceField(queryset=Schools.objects.all().order_by('schools_name'), initial=0)
        
        
class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = "__all__"
        labels = {
            'schools_id': 'Schools',
            'classes_id':'Classes'
        }
        school = forms.ModelChoiceField(queryset=Schools.objects.all().order_by('schools_name'), initial=0)
        classes = forms.ModelChoiceField(queryset=Classes.objects.all().order_by('class_name'), initial=0)
    
        
class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = "__all__"
        labels = {
            'courses_id':'Courses',
            'correct_answer':'correct_answer'
        }
        widgets = {
            'questions_name': forms.Textarea(attrs={'cols': 10, 'rows': 5}),
        }
     
        
class AnswersForm(forms.ModelForm):
    class Meta:
        model = Answers
        fields = "__all__"
        widgets = {
            'answers_name': forms.Textarea(attrs={'cols': 10, 'rows': 5}),
        }
         
        
class MyAnswersForm(forms.ModelForm):
    class Meta:
        model = MyAnswers
        fields = "__all__"

        
