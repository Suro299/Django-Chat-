# Generated by Django 4.2 on 2023-04-19 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_customuser_email_customuser_pic_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='pic',
            new_name='avatar',
        ),
        migrations.AddField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default='', max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='', max_length=255, unique=True, verbose_name='User name'),
        ),
    ]