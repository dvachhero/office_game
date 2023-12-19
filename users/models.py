from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Division(models.Model):
    name = models.CharField(max_length=100)  # Название дивизиона

    def __str__(self):
        return self.name


class Position(models.Model):
    title = models.CharField(max_length=100)  # Название должности

    def __str__(self):
        return self.title


class ResponsiblePerson(models.Model):
    full_name = models.CharField(max_length=200)  # Полное ФИО
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)  # Должность
    bitrix_id = models.CharField(max_length=100)  # ID в системе Битрикс
    city = models.CharField(max_length=100)  # Город
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, null=True)  # Дивизион

    def __str__(self):
        return self.full_name


class UserProfiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')  # Связь с моделью пользователя Django
    full_name = models.CharField(max_length=200)  # Полное ФИО
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, null=True)  # Дивизион
    city = models.CharField(max_length=100)  # Город
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)  # Должность
    responsible_person = models.ForeignKey(ResponsiblePerson, on_delete=models.SET_NULL,
                                           null=True)  # Ответственное лицо
    bitrix_id = models.CharField(max_length=100, null=True, blank=True)  # ID в системе Битрикс
    last_question_id = models.IntegerField(default=0)
    last_question_id_kmb = models.IntegerField(default=0)

    def __str__(self):
        return self.full_name

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfiles.objects.create(user=instance, last_question_id=0, last_question_id_kmb=0)
    else:
        instance.profile.save()
