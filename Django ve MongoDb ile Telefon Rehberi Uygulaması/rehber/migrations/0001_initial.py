# Generated by Django 2.2.5 on 2019-09-05 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rehber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('surname', models.CharField(max_length=120)),
                ('number', models.IntegerField()),
                ('address', models.CharField(max_length=120)),
            ],
        ),
    ]
