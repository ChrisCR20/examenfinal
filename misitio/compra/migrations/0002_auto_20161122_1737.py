# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='existencia',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(default=1.0, max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='producto',
            name='codigo',
            field=models.IntegerField(default=0),
        ),
    ]
