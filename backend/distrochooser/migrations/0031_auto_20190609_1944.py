# Generated by Django 2.1.2 on 2019-06-09 17:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distrochooser', '0030_auto_20190530_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='additionalInfo',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='usersession',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 9, 19, 44, 15, 439129)),
        ),
    ]
