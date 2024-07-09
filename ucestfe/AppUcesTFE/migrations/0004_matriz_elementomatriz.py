# Generated by Django 4.0.4 on 2024-07-04 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppUcesTFE', '0003_alter_proyecto_precision'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matriz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proyecto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AppUcesTFE.proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='ElementoMatriz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fila', models.IntegerField()),
                ('columna', models.IntegerField()),
                ('valor', models.IntegerField()),
                ('matriz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppUcesTFE.matriz')),
            ],
        ),
    ]