# Generated by Django 3.0.5 on 2020-09-10 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_remove_todo_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='description',
        ),
    ]