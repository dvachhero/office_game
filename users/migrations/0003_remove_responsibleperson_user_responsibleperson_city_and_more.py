# Generated by Django 5.0 on 2023-12-19 07:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_responsibleperson_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responsibleperson',
            name='user',
        ),
        migrations.AddField(
            model_name='responsibleperson',
            name='city',
            field=models.CharField(default='Неизвестный', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='responsibleperson',
            name='division',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.division'),
        ),
    ]
