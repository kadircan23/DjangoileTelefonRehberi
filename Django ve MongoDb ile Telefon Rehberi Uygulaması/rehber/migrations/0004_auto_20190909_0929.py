# Generated by Django 2.2.5 on 2019-09-09 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rehber', '0003_auto_20190906_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rehber',
            name='number',
            field=models.IntegerField(max_length=10, verbose_name='Tel No'),
        ),
    ]
