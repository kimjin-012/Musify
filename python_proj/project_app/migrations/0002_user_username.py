# Generated by Django 2.2.4 on 2021-04-17 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=True, max_length=50),
        ),
    ]
