# Generated by Django 4.2 on 2023-05-06 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incomes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='category',
            field=models.CharField(max_length=50),
        ),
    ]
