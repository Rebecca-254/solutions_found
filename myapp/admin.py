

# Register your models here.
from django.contrib import admin
from .models import Question, Answer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'views', 'get_answer_count']
    list_filter = ['created_at', 'is_anonymous']
    search_fields = ['title', 'content', 'author__username']
    readonly_fields = ['views', 'created_at', 'updated_at']

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['question', 'author', 'created_at', 'is_accepted']
    list_filter = ['created_at', 'is_anonymous', 'is_accepted']
    search_fields = ['content', 'author__username', 'question__title']
    readonly_fields = ['created_at', 'updated_at']

# ===== TEMPLATES =====