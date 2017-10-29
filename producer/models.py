# coding=utf-8
from django.db import models


class FunctionMapping(models.Model):
    serial_number = models.CharField('编号', max_length=200)
    function = models.CharField('模块', max_length=200)
    name = models.CharField('名称', max_length=200)

    class Meta:
        verbose_name_plural = u'模块列表'
        db_table = 'function_mapping'

    def __unicode__(self):  # __str__ on Python 3
        return self.name
