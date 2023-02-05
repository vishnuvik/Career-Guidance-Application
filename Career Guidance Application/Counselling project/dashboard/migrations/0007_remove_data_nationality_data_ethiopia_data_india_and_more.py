# Generated by Django 4.1.1 on 2023-02-05 06:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_rename_height_data_rank_remove_data_age_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='Nationality',
        ),
        migrations.AddField(
            model_name='data',
            name='Ethiopia',
            field=models.PositiveIntegerField(null=True, verbose_name=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='data',
            name='India',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='data',
            name='Nepal',
            field=models.PositiveIntegerField(null=True, verbose_name=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
    ]
