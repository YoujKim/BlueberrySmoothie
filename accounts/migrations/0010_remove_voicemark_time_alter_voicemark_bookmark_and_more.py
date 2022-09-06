# Generated by Django 4.0.6 on 2022-08-25 04:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voice', '0004_script'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0009_remove_voicemark_bookmark_voicemark_bookmark'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voicemark',
            name='time',
        ),
        migrations.AlterField(
            model_name='voicemark',
            name='bookmark',
            field=models.ManyToManyField(blank=True, related_name='bookmark', to='voice.voice'),
        ),
        migrations.AlterField(
            model_name='voicemark',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bookmark', to=settings.AUTH_USER_MODEL),
        ),
    ]