# Generated by Django 4.1.4 on 2022-12-26 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("distrochooser", "0068_givenanswer_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="additionalText",
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
