# Generated by Django 4.0.6 on 2022-09-29 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voice', '0010_alter_script_text_alter_voice_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='voice',
            name='script',
            field=models.FileField(blank=True, upload_to='script'),
        ),
        migrations.DeleteModel(
            name='script',
        ),
    ]
