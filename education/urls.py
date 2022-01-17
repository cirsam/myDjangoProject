from django.urls import path

from . import views

app_name = 'education'

urlpatterns = [
    path('', views.IndexView.as_view(),name="index"),
    path('setuserType/', views.set_user_type, name='set_user_type'),
    path('schools/', views.SchoolsIndexView.as_view(),name="schools_index"),
    path('schools/edit/<int:pk>/', views.schools_edit, name='schools_edit'),
    path('schools/create/', views.schools_create, name='schools_create'),
    path('schools/delete/<int:pk>/', views.schools_delete, name='schools_delete'),
    path('class/', views.ClassesIndexView.as_view(),name="class_index"),
    path('class/edit/<int:pk>/', views.class_edit, name='class_edit'),
    path('class/create/', views.class_create, name='class_create'),
    path('class/delete/<int:pk>/', views.class_delete, name='class_delete'),
    path('courses/', views.CoursesIndexView.as_view(),name="courses_index"),
    path('courses/edit/<int:pk>/', views.courses_edit, name='courses_edit'),
    path('courses/details/<int:pk>/', views.CoursesDetailsView.as_view(), name='courses_details'),
    path('courses/create/', views.courses_create, name='courses_create'),
    path('courses/delete/<int:pk>/', views.courses_delete, name='courses_delete'),
    path('questions/', views.QuestionsIndexView.as_view(),name="questions_index"),
    path('questions/edit/<int:pk>/', views.questions_edit, name='questions_edit'),
    path('questions/CorrectAnswer/<int:pk>/', views.questions_Correct_answer, name='correct_answer'),
    path('questions/details/<int:pk>/', views.QuestionsDetailsView.as_view(), name='questions_details'),
    path('questions/create/courses/<int:courses_id>/', views.QuestionsCreateView.as_view(), name='questions_create'),
    path('questions/delete/<int:pk>/', views.questions_delete, name='questions_delete'),
    path('answers/', views.AnswersIndexView.as_view(),name="answers_index"),
    path('answers/edit/<int:pk>/', views.answers_edit, name='answers_edit'),
    path('answers/create/questions/<int:questions_id>/', views.AnswersCreateView.as_view(), name='answers_create'),
    path('answers/delete/<int:pk>/', views.answers_delete, name='answers_delete'),
    
    #Exams URLS 
     path('getschools/', views.get_schools, name='getschools'),
     path('getclasses/<int:pk>', views.get_classes, name='getclasses'),
     path('getcourses/schools/<int:schools_pk>/classes/<int:classes_pk>', views.get_courses, name='getcourses'),
     path('myexams/schools/<int:schools_pk>/classes/<int:classes_pk>/courses/<int:courses_pk>', views.MyExamsView.as_view(), name='my_exams'),
     path('getanswers/<int:questions_pk>', views.get_answers, name='getanswers'),
     path('saveanswers/', views.save_answers, name='saveanswers'),
     path('finish/schools/<int:schools_id>/classes/<int:classes_id>/courses/<int:courses_id>/session/<int:session_id>', views.finish_answers, name='finish'),
     path('printCertificate/schools/<int:schools_id>/classes/<int:classes_id>/courses/<int:courses_id>/session/<int:session_id>/fullname/<str:fullname>/', views.print_certificate, name='printCertificate'),
  
]