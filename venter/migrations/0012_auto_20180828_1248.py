# Generated by Django 2.0.7 on 2018-08-28 07:18

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_auto_20180401_2303'),
        ('venter', '0011_auto_20180827_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 28, 7, 18, 29, 615723, tzinfo=utc)),
        ),
        migrations.RemoveField(
            model_name='complaints',
            name='media',
        ),
        migrations.AddField(
            model_name='complaints',
            name='media',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='media', to='upload.UploadedImage'),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='report_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 28, 7, 18, 29, 615723, tzinfo=utc)),
        ),
    ]
