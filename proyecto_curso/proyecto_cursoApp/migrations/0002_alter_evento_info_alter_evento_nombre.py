# Generated by Django 4.0.5 on 2022-06-22 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto_cursoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='info',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='evento',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
