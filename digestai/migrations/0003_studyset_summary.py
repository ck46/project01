# Generated by Django 3.2.6 on 2021-09-02 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digestai', '0002_auto_20210901_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='studyset',
            name='summary',
            field=models.CharField(default='', max_length=500),
        ),
    ]
