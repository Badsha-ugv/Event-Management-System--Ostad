# Generated by Django 5.1.2 on 2024-10-30 11:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_alter_event_date_alter_event_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 30, 11, 15, 48, 299639, tzinfo=datetime.timezone.utc)),
        ),
    ]