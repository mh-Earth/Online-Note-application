# Generated by Django 3.2.5 on 2022-02-09 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='', max_length=32),
        ),
    ]