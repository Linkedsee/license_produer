# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producer', '0003_functionmapping_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='functionmapping',
            options={'verbose_name_plural': '\u6a21\u5757\u5217\u8868'},
        ),
        migrations.AlterModelTable(
            name='functionmapping',
            table='function_mapping',
        ),
    ]
