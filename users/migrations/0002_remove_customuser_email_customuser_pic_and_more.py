# Generated by Django 4.2 on 2023-04-19 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='email',
        ),
        migrations.AddField(
            model_name='customuser',
            name='pic',
            field=models.ImageField(default='', upload_to='', verbose_name='User Avatar'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='', max_length=255, unique=True, verbose_name='Username'),
        ),
    ]
