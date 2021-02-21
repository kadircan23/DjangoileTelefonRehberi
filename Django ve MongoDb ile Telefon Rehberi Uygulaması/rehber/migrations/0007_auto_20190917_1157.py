# Generated by Django 2.2.5 on 2019-09-17 08:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rehber', '0006_auto_20190917_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rehber',
            name='number',
            field=models.PositiveIntegerField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='Tel No'),
        ),
    ]
