# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_firstname', models.CharField(max_length=256)),
                ('user_lastname', models.CharField(max_length=256)),
                ('user_cards', models.ManyToManyField(to='collection.Card')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_image',
            field=models.ImageField(upload_to=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='team_image',
            field=models.ImageField(upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
