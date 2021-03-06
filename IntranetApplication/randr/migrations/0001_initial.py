# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 13:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Associate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('is_manager', models.BooleanField()),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reportingmgr', to='randr.Associate')),
            ],
        ),
        migrations.CreateModel(
            name='Recognition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('A', 'Normal'), ('H', 'Hidden'), ('D', 'Deleted')], default='N', max_length=1)),
                ('annotation_title', models.CharField(max_length=200)),
                ('annotation_desc', models.TextField(max_length=200)),
                ('associate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='associate', to='randr.Associate')),
                ('recognition_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recognizedby', to='randr.Associate')),
            ],
        ),
    ]
