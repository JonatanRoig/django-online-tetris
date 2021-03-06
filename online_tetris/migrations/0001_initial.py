# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-01 12:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Castigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Sesion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='codigo')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('puntos', models.IntegerField(default=0)),
                ('velocidad', models.IntegerField(default=100)),
                ('ip', models.GenericIPAddressField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AddField(
            model_name='castigo',
            name='emisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emisor', to='online_tetris.Sesion'),
        ),
        migrations.AddField(
            model_name='castigo',
            name='receptor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receptor', to='online_tetris.Sesion'),
        ),
    ]
