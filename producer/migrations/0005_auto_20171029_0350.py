# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producer', '0004_auto_20171028_0726'),
    ]

    operations = [
        migrations.CreateModel(
            name='LicenseHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer', models.CharField(max_length=200, verbose_name=b'\xe5\xae\xa2\xe6\x88\xb7')),
                ('function', models.CharField(max_length=200, verbose_name=b'\xe6\x8e\x88\xe6\x9d\x83\xe6\xa8\xa1\xe5\x9d\x97')),
                ('effective_time', models.CharField(max_length=200, verbose_name=b'\xe6\x9c\x89\xe6\x95\x88\xe6\x9c\x9f')),
                ('kind', models.CharField(max_length=200, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'db_table': 'license_history',
                'verbose_name_plural': '\u6a21\u5757\u5217\u8868',
            },
        ),
        migrations.AlterField(
            model_name='functionmapping',
            name='function',
            field=models.CharField(max_length=200, verbose_name=b'\xe6\xa8\xa1\xe5\x9d\x97'),
        ),
        migrations.AlterField(
            model_name='functionmapping',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='functionmapping',
            name='serial_number',
            field=models.CharField(max_length=200, verbose_name=b'\xe7\xbc\x96\xe5\x8f\xb7'),
        ),
    ]
