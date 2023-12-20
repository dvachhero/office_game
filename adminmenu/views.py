from django.shortcuts import render
from users.models import UserProfiles
from game.models import AnswerOfficeGame

def admin_menu(request):
    return render(request, 'admin_menu.html')

def send_message_b24(request):
    profiles = UserProfiles.objects.all()
    return render(request, 'send_message_b24.html', {'profiles': profiles})

def send_result_b24(request):
    # Получение данных об ответах и соответствующих пользователях
    answers_data = AnswerOfficeGame.objects.select_related('user__profile', 'question').all()

    # Подготовка данных для вывода в шаблон
    results = []
    user_correct_answers = {}  # Словарь для подсчета правильных ответов пользователя

    for answer in answers_data:
        user_id = answer.user.id
        if user_id not in user_correct_answers:
            user_correct_answers[user_id] = {'correct': 0, 'incorrect': 0}

        # Подсчет правильных и неправильных ответов
        if answer.answer == answer.right_answer:
            user_correct_answers[user_id]['correct'] += 1
        else:
            user_correct_answers[user_id]['incorrect'] += 1

        # Формирование данных для таблицы
        results.append({
            'full_name': answer.user.profile.full_name,
            'bitrix_id': answer.user.profile.bitrix_id,
            'question_text': answer.question.question_text,
            'user_answer': answer.answer,
            'right_answer': answer.right_answer,
            'user_correct_answers': user_correct_answers[user_id]
        })

    return render(request, 'send_result_b24.html', {'results': results})