# Generated by Django 4.0.4 on 2024-07-05 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUcesTFE', '0004_matriz_elementomatriz'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='cuadrante1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='cuadrante2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='cuadrante3',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='cuadrante4',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
