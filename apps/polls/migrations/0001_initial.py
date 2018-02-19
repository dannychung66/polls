# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-09 14:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_name', models.CharField(max_length=100)),
                ('candidate_no', models.CharField(max_length=100)),
                ('party', models.CharField(max_length=100)),
                ('remarks', models.TextField()),
                ('img_link', models.TextField()),
                ('no_of_vote', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voter_name', models.CharField(blank=True, max_length=100)),
                ('voter_text', models.TextField(blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Candidate')),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.District'),
        ),
    ]