# Generated by Django 5.0.3 on 2024-07-11 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='Desc',
            new_name='Task_Desc',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='Title',
            new_name='Task_Title',
        ),
    ]
