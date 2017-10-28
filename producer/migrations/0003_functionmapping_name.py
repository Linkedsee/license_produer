# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producer', '0002_functionmapping_serial_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='functionmapping',
            name='name',
            field=models.CharField(default='\u8d44\u4ea7\u7ba1\u7406', max_length=200),
            preserve_default=False,
        ),
    ]
