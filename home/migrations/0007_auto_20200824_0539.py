# Generated by Django 2.2.15 on 2020-08-24 05:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("home", "0006_auto_20200824_0536"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="key1",
            field=models.ForeignKey(
                blank=True,
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                related_name="homepage_key1",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="key2",
            field=models.ForeignKey(
                blank=True,
                default=2,
                null=True,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                related_name="homepage_key2",
                to="home.CustomText",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="key3",
            field=models.OneToOneField(
                blank=True,
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                related_name="homepage_key3",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="key4",
            field=models.OneToOneField(
                blank=True,
                default=4,
                null=True,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                related_name="homepage_key4",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
