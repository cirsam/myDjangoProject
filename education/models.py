from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
class Schools(models.Model):
    schools_id = models.AutoField(primary_key=True)
    schools_name = models.CharField(max_length=200)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    userId = models.CharField(max_length=50, default='1', editable=False)
    website = models.URLField()
    pub_date = models.DateTimeField('date published', default='', editable=False)
    
    class Meta:
        ordering = ["-schools_name"]
        
    def __str__(self):
        return self.schools_name
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        
        
class Classes(models.Model):
    class_name = models.CharField(max_length=200)
    schools = models.ForeignKey(Schools, on_delete=models.SET_NULL, null=True)
    userId = models.CharField(max_length=50, default='1', editable=False)
    pub_date = models.DateTimeField('date published', default='', editable=False)
    
    class Meta:
        ordering = ["-class_name"]
        
    def __str__(self):
        return self.class_name
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        
        
class Courses(models.Model):
    courses_name = models.CharField(max_length=200)
    schools = models.ForeignKey(Schools, on_delete=models.SET_NULL, null=True)
    classes = models.ForeignKey(Classes, on_delete=models.SET_NULL, null=True)
    userId = models.CharField(max_length=50, default='1', editable=False)
    pub_date = models.DateTimeField('date published', default='', editable=False)
    
    class Meta:
        ordering = ["-courses_name"]
        
    def __str__(self):
        return self.courses_name
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)        
   
   
class Questions(models.Model):
    questions_name = models.CharField(max_length=200)
    courses_id = models.CharField(max_length=20, default='1', editable=False)
    userId = models.CharField(max_length=50, default='1', editable=False)
    correct_answer = models.CharField(max_length=50, default='1', editable=False)
    pub_date = models.DateTimeField('date published', default='', editable=False)
    
    class Meta:
        ordering = ["-questions_name"]
        
    def __str__(self):
        return self.questions_name
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)   
 
 
class Answers(models.Model):
    answers_name = models.CharField(max_length=200)
    questions = models.ForeignKey(Questions, on_delete=models.SET_NULL, null=True,editable=False)
    userId = models.CharField(max_length=50, default='1', editable=False)
    pub_date = models.DateTimeField('date published', default='', editable=False)
    
    class Meta:
        ordering = ["-answers_name"]
        
    def __str__(self):
        return self.answers_name
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) 
 
 
 
class MyAnswers(models.Model):
    questions = models.ForeignKey(Questions, on_delete=models.SET_NULL, null=True,editable=False)
    answers = models.ForeignKey(Answers, on_delete=models.SET_NULL, null=True,editable=False)
    test_session = models.CharField(max_length=50, default='1', editable=False)
    userId = models.CharField(max_length=50, default='1', editable=False)
    pub_date = models.DateTimeField('date published', default='', editable=False)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)