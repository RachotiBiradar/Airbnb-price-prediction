# Generated by Django 2.2.1 on 2019-05-12 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='price',
        ),
    ]
