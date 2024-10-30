# Generated by Django 5.1.2 on 2024-10-30 03:05

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_event_participants_alter_event_date_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 30, 3, 5, 13, 253345, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(blank=True, null=True, related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
    ]