# Generated by Django 5.0.1 on 2024-12-07 19:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nudge', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='nudges',
            new_name='nudge',
        ),
    ]
