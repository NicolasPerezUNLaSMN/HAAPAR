# Generated by Django 4.0.4 on 2024-07-12 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppUcesTFE', '0009_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
    ]
