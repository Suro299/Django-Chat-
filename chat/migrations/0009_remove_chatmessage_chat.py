# Generated by Django 4.1.6 on 2023-06-01 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_remove_chat_member_1_remove_chat_member_2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmessage',
            name='chat',
        ),
    ]
