# Generated by Django 4.0.4 on 2024-07-08 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUcesTFE', '0006_matrizcuadrada_elementomatrizcuadrada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variablebd',
            name='dependencia1',
        ),
        migrations.RemoveField(
            model_name='variablebd',
            name='dependencia2',
        ),
        migrations.RemoveField(
            model_name='variablebd',
            name='dependencia5',
        ),
        migrations.RemoveField(
            model_name='variablebd',
            name='influencia1',
        ),
        migrations.RemoveField(
            model_name='variablebd',
            name='influencia2',
        ),
        migrations.RemoveField(
            model_name='variablebd',
            name='influencia5',
        ),
        migrations.AddField(
            model_name='variablebd',
            name='tipo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('objetivo', models.CharField(max_length=100)),
                ('numeros', models.CharField(max_length=100)),
                ('proyecto', models.ManyToManyField(to='AppUcesTFE.proyecto')),
            ],
        ),
    ]
