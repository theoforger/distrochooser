# Generated by Django 4.1.4 on 2023-01-04 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("distrochooser", "0078_distribution_data_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="distribution",
            name="version",
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="distribution",
            name="data_id",
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
    ]
