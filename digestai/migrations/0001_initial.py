# Generated by Django 3.2.6 on 2021-09-01 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudySet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('school_name', models.CharField(max_length=100)),
            ],
        ),
    ]