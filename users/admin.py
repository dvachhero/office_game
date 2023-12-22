from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
import requests
from urllib.parse import quote
from .models import Division, Position, ResponsiblePerson, UserProfiles



@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(ResponsiblePerson)
class ResponsiblePersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'bitrix_id', 'city', 'division')
    search_fields = ('full_name', 'bitrix_id', 'city')
    list_filter = ('position', 'city', 'division')

@admin.register(UserProfiles)
class UserProfilesAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'division', 'city', 'position', 'responsible_person', 'bitrix_id', 'last_question_id', 'last_question_id_kmb')
    search_fields = ('full_name', 'city', 'bitrix_id', 'last_question_id', 'last_question_id_kmb')
    list_filter = ('division', 'position', 'city', 'last_question_id', 'last_question_id_kmb')