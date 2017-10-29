# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producer', '0005_auto_20171029_0350'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='licensehistory',
            options={'verbose_name_plural': 'license \u5386\u53f2\u8bb0\u5f55'},
        ),
        migrations.AddField(
            model_name='licensehistory',
            name='asset_num',
            field=models.IntegerField(default=100, verbose_name=b'\xe6\x8e\x88\xe6\x9d\x83\xe6\x95\xb0\xe9\x87\x8f'),
            preserve_default=False,
        ),
    ]
