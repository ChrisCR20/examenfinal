# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0002_auto_20161122_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='compra',
            name='codigo_p',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='compra',
            name='fecha',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
