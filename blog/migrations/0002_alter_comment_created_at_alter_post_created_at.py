# Generated by Django 4.1.7 on 2023-03-22 18:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 22, 18, 42, 20, 943712, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 22, 18, 42, 20, 943164, tzinfo=datetime.timezone.utc)),
        ),
    ]