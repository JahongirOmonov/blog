# Generated by Django 4.2.7 on 2024-05-28 16:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_post_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="is_recommended",
            field=models.BooleanField(default=False),
        ),
    ]
