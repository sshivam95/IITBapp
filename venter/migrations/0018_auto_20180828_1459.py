# Generated by Django 2.0.7 on 2018-08-28 09:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('venter', '0017_auto_20180828_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 28, 9, 29, 44, 129905, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='report_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 28, 9, 29, 44, 128905, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='status',
            field=models.CharField(choices=[('reported', 'Reported'), ('in_progress', 'In Progress'), ('resolved', 'Resolved'), ('delete', 'Delete')], default='reported', max_length=30),
        ),
    ]
