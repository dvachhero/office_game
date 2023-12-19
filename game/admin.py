from django.contrib import admin
from .models import (
    QuestionOfficeGame, AnswerOfficeGame, QuestionTraining, AnswerTraining,
    KmbQuestionOffice, KmbAnswerOffice, UserResultsAccess, UserResultsKmbAccess
)

# Регистрация модели вопросов для игры в офисе
@admin.register(QuestionOfficeGame)
class QuestionOfficeGameAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'correct_answer')
    search_fields = ('question_text',)

# Регистрация модели ответов для игры в офисе
@admin.register(AnswerOfficeGame)
class AnswerOfficeGameAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'answer', 'right_answer')
    search_fields = ('user__username', 'question__question_text')

# Регистрация модели вопросов для тренировки
@admin.register(QuestionTraining)
class QuestionTrainingAdmin(admin.ModelAdmin):
    list_display = ('question_text',)
    search_fields = ('question_text',)

# Регистрация модели ответов для тренировки
@admin.register(AnswerTraining)
class AnswerTrainingAdmin(admin.ModelAdmin):
    list_display = ('user', 'selected_answer', 'is_correct', 'correct_sequence')
    search_fields = ('user__username',)

# Регистрация модели вопросов КМБ
@admin.register(KmbQuestionOffice)
class KmbQuestionOfficeAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'correct_answer')
    search_fields = ('question_text',)

# Регистрация модели ответов КМБ
@admin.register(KmbAnswerOffice)
class KmbAnswerOfficeAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'answer', 'right_answer')
    search_fields = ('user__username', 'question__question_text')

# Регистрация модели доступа к результатам пользователя
@admin.register(UserResultsAccess)
class UserResultsAccessAdmin(admin.ModelAdmin):
    list_display = ('is_access_enabled',)

# Регистрация модели доступа к результатам КМБ пользователя
@admin.register(UserResultsKmbAccess)
class UserResultsKmbAccessAdmin(admin.ModelAdmin):
    list_display = ('is_access_enabled',)
