# Generated by Django 4.1.6 on 2023-06-01 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_remove_chat_members_chat_member_1_chat_member_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='messages',
            field=models.ManyToManyField(blank=True, related_name='chat_messages', to='chat.chatmessage'),
        ),
    ]
