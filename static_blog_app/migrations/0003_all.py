# Generated by Django 5.0.3 on 2024-04-11 16:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("static_blog_app", "0002_writ"),
    ]

    operations = [
        migrations.CreateModel(
            name="all",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "stock",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="static_blog_app.des",
                    ),
                ),
            ],
        ),
    ]
