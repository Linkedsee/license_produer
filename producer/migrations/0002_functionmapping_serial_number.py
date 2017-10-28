# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='functionmapping',
            name='serial_number',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
