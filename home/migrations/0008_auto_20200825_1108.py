# Generated by Django 2.2.15 on 2020-08-25 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0007_auto_20200824_0539"),
    ]

    operations = [
        migrations.RemoveField(model_name="customtext", name="key1",),
        migrations.RemoveField(model_name="customtext", name="key2",),
        migrations.RemoveField(model_name="customtext", name="new",),
        migrations.RemoveField(model_name="customtext", name="test",),
        migrations.RemoveField(model_name="customtext", name="tests",),
        migrations.RemoveField(model_name="customtext", name="user",),
        migrations.RemoveField(model_name="homepage", name="key1",),
        migrations.RemoveField(model_name="homepage", name="key2",),
        migrations.RemoveField(model_name="homepage", name="key3",),
        migrations.RemoveField(model_name="homepage", name="key4",),
    ]
