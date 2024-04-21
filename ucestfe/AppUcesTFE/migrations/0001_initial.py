# Generated by Django 4.0.4 on 2024-03-31 01:07

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
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tema', models.CharField(max_length=500)),
                ('hasta', models.IntegerField(blank=True, null=True)),
                ('precision', models.IntegerField(blank=True, null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('nombre_corto', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=1000)),
                ('importancia', models.IntegerField(blank=True, null=True)),
                ('incertidumbre', models.IntegerField(blank=True, null=True)),
                ('influencia1', models.FloatField(blank=True, null=True)),
                ('dependencia1', models.FloatField(blank=True, null=True)),
                ('influencia2', models.FloatField(blank=True, null=True)),
                ('dependencia2', models.FloatField(blank=True, null=True)),
                ('influencia5', models.FloatField(blank=True, null=True)),
                ('dependencia5', models.FloatField(blank=True, null=True)),
                ('categoria', models.CharField(max_length=100)),
                ('numeros', models.CharField(max_length=100)),
                ('tendencias', models.CharField(max_length=1000)),
                ('proyecto', models.ManyToManyField(to='AppUcesTFE.proyecto')),
            ],
        ),
    ]
