# Generated by Django 4.1.6 on 2023-06-01 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0007_alter_chat_member_1_alter_chat_member_2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='member_1',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='member_2',
        ),
        migrations.AddField(
            model_name='chat',
            name='member_1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='member1', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chat',
            name='member_2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='member2', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]