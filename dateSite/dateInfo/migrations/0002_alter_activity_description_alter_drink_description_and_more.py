# Generated by Django 4.1.6 on 2023-02-13 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dateInfo", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="activity",
            name="description",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="drink",
            name="description",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="food",
            name="description",
            field=models.TextField(blank=True),
        ),
    ]