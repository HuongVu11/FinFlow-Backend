# Generated by Django 4.2 on 2023-04-29 03:44

import datetime
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
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('salary', 'Salary'), ('freelance', 'Freelance'), ('investment', 'Investment'), ('rental', 'Rental'), ('grant', 'Grant'), ('other', 'Other')], max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('amount', models.PositiveIntegerField()),
                ('date', models.DateField(default=datetime.date.today)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
