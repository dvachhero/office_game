from django.db import models
from django.contrib.auth.models import User


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
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Связь с моделью пользователя Django
    full_name = models.CharField(max_length=200)  # Полное ФИО
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, null=True)  # Дивизион
    city = models.CharField(max_length=100)  # Город
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)  # Должность
    responsible_person = models.ForeignKey(ResponsiblePerson, on_delete=models.SET_NULL,
                                           null=True)  # Ответственное лицо
    bitrix_id = models.CharField(max_length=100, null=True, blank=True)  # ID в системе Битрикс

    def __str__(self):
        return self.full_name
