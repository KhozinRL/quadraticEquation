# Generated by Django 3.2.3 on 2021-05-24 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quadraticEquationApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equation',
            name='x1',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='equation',
            name='x2',
            field=models.FloatField(null=True),
        ),
    ]
