# Generated by Django 4.0.6 on 2022-08-25 05:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voice', '0004_script'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0010_remove_voicemark_time_alter_voicemark_bookmark_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history', models.ManyToManyField(blank=True, related_name='history', to='voice.voice')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='history', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
