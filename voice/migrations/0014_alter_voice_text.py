# Generated by Django 4.0.6 on 2022-09-29 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voice', '0013_voice_script_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voice',
            name='text',
            field=models.TextField(default=''),
        ),
    ]