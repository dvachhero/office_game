from django.contrib import admin
from .models import Division, Position, ResponsiblePerson, UserProfiles

# Регистрируем модель Division для админ-панели
@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Поля для отображения в списке
    search_fields = ('name',)  # Поля для поиска

# Регистрируем модель Position для админ-панели
@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

# Регистрируем модель ResponsiblePerson для админ-панели
@admin.register(ResponsiblePerson)
class ResponsiblePersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'bitrix_id', 'city', 'division')
    search_fields = ('full_name', 'bitrix_id', 'city')
    list_filter = ('position', 'city', 'division')

# Регистрируем модель UserProfiles для админ-панели
@admin.register(UserProfiles)
class UserProfilesAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'division', 'city', 'position', 'last_question_id', 'last_question_id_kmb', 'responsible_person', 'bitrix_id')
    search_fields = ('full_name', 'city', 'last_question_id', 'last_question_id_kmb', 'bitrix_id')
    list_filter = ('division', 'position',  'city', 'last_question_id', 'last_question_id_kmb')

