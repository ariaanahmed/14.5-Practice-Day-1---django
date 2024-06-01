# Generated by Django 5.0.6 on 2024-06-01 06:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_student_date_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date_time_field',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]