# Generated by Django 5.0.3 on 2024-07-11 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Desc', models.TextField()),
                ('Time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
