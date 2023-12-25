from django.shortcuts import render
from users.models import UserProfiles, ResponsiblePerson
from game.models import AnswerOfficeGame, AnswerTraining, KmbAnswerOffice

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

    results = sorted(results, key=lambda x: (x['full_name'], x['question_text']))

    return render(request, 'send_result_b24.html', {'results': results})

def send_result_training_b24(request):
    answers = AnswerTraining.objects.select_related('user').all()

    results = []
    for answer in answers:
        user_profile = UserProfiles.objects.filter(user=answer.user).first()

        if user_profile:
            responsible_person = ResponsiblePerson.objects.filter(id=user_profile.responsible_person_id).first()
            result = {
                'full_name': user_profile.full_name,
                'division': user_profile.division.name if user_profile.division else '',
                'position': user_profile.position.title if user_profile.position else '',
                'bitrix_id': user_profile.bitrix_id,
                'correct_sequence': answer.correct_sequence,
                'responsible': {
                    'full_name': responsible_person.full_name if responsible_person else '',
                    'position': responsible_person.position.title if responsible_person and responsible_person.position else '',
                    'bitrix_id': responsible_person.bitrix_id if responsible_person else '',
                }
            }
            results.append(result)

    return render(request, 'send_result_training_b24.html', {'results': results})

def send_result_kmb_b24(request):
    kmb_answers_data = KmbAnswerOffice.objects.select_related('user__profile', 'question').all()

    results = []
    for answer in kmb_answers_data:
        user_profile = UserProfiles.objects.filter(user=answer.user).first()
        responsible_person = ResponsiblePerson.objects.filter(id=user_profile.responsible_person_id).first() if user_profile else None

        results.append({
            'full_name': user_profile.full_name if user_profile else 'Неизвестный пользователь',
            'bitrix_id': user_profile.bitrix_id if user_profile else 'Нет ID',
            'question_text': answer.question.question_text,
            'user_answer': answer.answer,
            'right_answer': answer.right_answer,
            'responsible': {
                'full_name': responsible_person.full_name if responsible_person else '',
                'position': responsible_person.position.title if responsible_person and responsible_person.position else '',
                'bitrix_id': responsible_person.bitrix_id if responsible_person else '',
            }
        })

    return render(request, 'send_result_kmb_b24.html', {'results': results})
