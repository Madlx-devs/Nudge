# Generated by Django 5.0.1 on 2024-12-07 19:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='nudges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('images', models.ImageField(upload_to='static/media')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nudges', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
