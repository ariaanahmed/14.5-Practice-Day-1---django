# Generated by Django 5.0.6 on 2024-06-01 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date_field',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
    ]
