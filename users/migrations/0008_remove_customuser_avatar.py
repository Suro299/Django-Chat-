# Generated by Django 4.1.6 on 2023-06-01 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_customuser_avatar_alter_customuser_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='avatar',
        ),
    ]
