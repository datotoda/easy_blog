# Generated by Django 4.1 on 2022-08-04 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Color",
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
                    "value",
                    models.CharField(
                        max_length=20, unique=True, verbose_name="Color value"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
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
                    "value",
                    models.CharField(
                        max_length=40, unique=True, verbose_name="Tag value"
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name=""),
                ),
                (
                    "color",
                    models.ForeignKey(
                        on_delete=models.SET(""), related_name="tags", to="blog.color"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Post",
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
                    "title",
                    models.CharField(
                        max_length=40, unique=True, verbose_name="Post title"
                    ),
                ),
                ("value", models.TextField(verbose_name="Post value")),
                (
                    "image_url",
                    models.URLField(blank=True, verbose_name="Post thumbnail url"),
                ),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name=""),
                ),
                (
                    "tags",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="posts",
                        to="blog.tag",
                        verbose_name="Post tags",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("value", models.TextField(verbose_name="Comment value")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name=""),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="blog.post",
                        verbose_name="Post",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
        ),
    ]