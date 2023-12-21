# Generated by Django 4.2.8 on 2023-12-21 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
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
                ("name", models.CharField(max_length=255, verbose_name="Name")),
                ("description", models.TextField(verbose_name="Description")),
                ("price", models.PositiveIntegerField(verbose_name="Price")),
            ],
            options={
                "verbose_name": "Item",
                "verbose_name_plural": "Items",
                "db_table": "items",
                "ordering": ["name"],
            },
        ),
    ]