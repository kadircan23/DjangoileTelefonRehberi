# Generated by Django 2.2.5 on 2019-09-17 08:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rehber', '0007_auto_20190917_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rehber',
            name='number',
            field=models.PositiveIntegerField(validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='Tel No'),
        ),
    ]
