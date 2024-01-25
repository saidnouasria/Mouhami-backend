# Generated by Django 5.0 on 2024-01-25 13:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Language",
            fields=[
                (
                    "name",
                    models.CharField(
                        max_length=255, primary_key=True, serialize=False, unique=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Specialities",
            fields=[
                (
                    "name",
                    models.CharField(
                        max_length=255, primary_key=True, serialize=False, unique=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Lawyer",
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
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=20)),
                ("photo", models.CharField(blank=True, max_length=255, null=True)),
                ("location", models.CharField(blank=True, max_length=255, null=True)),
                ("wilaya", models.CharField(blank=True, max_length=255, null=True)),
                ("lng", models.FloatField(blank=True, null=True)),
                ("lat", models.FloatField(blank=True, null=True)),
                ("rating", models.FloatField(blank=True, null=True)),
                (
                    "languages",
                    models.ManyToManyField(blank=True, to="mouhami_api.language"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "specialities",
                    models.ManyToManyField(blank=True, to="mouhami_api.specialities"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Booking",
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
                ("date", models.DateField()),
                ("time", models.TimeField()),
                (
                    "client_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "lawyer_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mouhami_api.lawyer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Review",
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
                ("rating", models.FloatField()),
                ("comment", models.TextField()),
                (
                    "booking",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mouhami_api.booking",
                    ),
                ),
                (
                    "lawyer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mouhami_api.lawyer",
                    ),
                ),
                (
                    "reviewer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]