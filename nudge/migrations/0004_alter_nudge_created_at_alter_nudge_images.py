# Generated by Django 5.0.1 on 2024-12-07 20:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nudge', '0003_alter_nudge_content_alter_nudge_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nudge',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nudge',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]