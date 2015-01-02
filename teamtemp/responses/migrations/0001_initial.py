# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamTemperature',
            fields=[
                ('id', models.CharField(default=b'AVakaYus', max_length=8, serialize=False, primary_key=True)),
                ('creation_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TemperatureResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField(verbose_name=b'Temperature (1-10)', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('word', models.CharField(max_length=32, verbose_name=b"One word to describe how you're feeling", validators=[django.core.validators.RegexValidator(regex=b"^[A-Za-z0-9'-]+$", message=b'please enter a single word with alphanumeric characters only.', code=b'Invalid Word')])),
                ('request', models.ForeignKey(to='responses.TeamTemperature')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=8, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='temperatureresponse',
            name='responder',
            field=models.ForeignKey(to='responses.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='teamtemperature',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
