# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('date', models.DateField()),
                ('create_date', models.DateTimeField(default=datetime.datetime.now)),
                ('author', models.ForeignKey(related_name='event', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Peer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('telephone_number', models.CharField(max_length=16, blank=True)),
                ('favorite_contact', models.NullBooleanField()),
                ('notes', models.CharField(max_length=100, blank=True)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now)),
                ('author', models.ForeignKey(related_name='peer', to=settings.AUTH_USER_MODEL)),
                ('event', models.ManyToManyField(to='peer_app.Event')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
    ]
