# Generated by Django 4.1.4 on 2023-01-04 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("distrochooser", "0081_distribution_age"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="tag_prexfix",
            field=models.CharField(blank=True, default=None, max_length=25, null=True),
        ),
    ]
