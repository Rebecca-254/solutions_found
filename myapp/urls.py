from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('ask/', views.ask_question, name='ask_question'),
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
    path('my-questions/', views.my_questions, name='my_questions'),
    path('my-answers/', views.my_answers, name='my_answers'),
]

