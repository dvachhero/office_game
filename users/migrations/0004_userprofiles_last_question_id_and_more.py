# Generated by Django 5.0 on 2023-12-19 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_responsibleperson_user_responsibleperson_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofiles',
            name='last_question_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofiles',
            name='last_question_id_kmb',
            field=models.IntegerField(default=0),
        ),
    ]
