from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm

def home(request):
    """Home page with all questions"""
    questions = Question.objects.all()
    search_query = request.GET.get('search', '')
    
    if search_query:
        questions = questions.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query)
        )
    
    context = {
        'questions': questions,
        'search_query': search_query,
    }
    return render(request, 'myapp/home.html', context)

@login_required
def ask_question(request):
    """Ask a new question"""
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            messages.success(request, 'Your question has been posted!')
            return redirect('question_detail', pk=question.pk)
    else:
        form = QuestionForm()
    
    return render(request, 'myapp/ask_question.html', {'form': form})

def question_detail(request, pk):
    """View a specific question and its answers"""
    question = get_object_or_404(Question, pk=pk)
    question.views += 1
    question.save()
    
    answers = question.answers.all()
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            messages.success(request, 'Your answer has been posted!')
            return redirect('myapp:question_detail', pk=question.pk)
    else:
        form = AnswerForm() if request.user.is_authenticated else None
    
    context = {
        'question': question,
        'answers': answers,
        'form': form,
    }
    return render(request, 'myapp/question_detail.html', context)

@login_required
def my_questions(request):
    """User's questions"""
    questions = Question.objects.filter(author=request.user)
    return render(request, 'myapp/my_questions.html', {'questions': questions})

@login_required
def my_answers(request):
    """User's answers"""
    answers = Answer.objects.filter(author=request.user)
    return render(request, 'myapp/my_answers.html', {'answers': answers})
