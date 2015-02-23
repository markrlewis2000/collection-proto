# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_auto_20150221_1855'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCards',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField()),
                ('cardid', models.ForeignKey(to='collection.Card')),
                ('userid', models.ForeignKey(to='collection.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_cards',
            field=models.ManyToManyField(to='collection.Card', through='collection.UserCards'),
            preserve_default=True,
        ),
    ]
