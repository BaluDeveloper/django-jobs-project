# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-04-04 05:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='delhijobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('eligibility', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='hydjobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('eligibility', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='punejobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('eligibility', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
            ],
        ),
    ]
