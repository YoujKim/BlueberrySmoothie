# Generated by Django 4.0.6 on 2022-09-16 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voice', '0008_script_text_string'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='script',
            name='text_string',
        ),
    ]
