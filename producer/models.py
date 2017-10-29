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


class LicenseHistory(models.Model):
    customer = models.CharField('客户', max_length=200)
    function = models.CharField('授权模块', max_length=200)
    effective_time = models.CharField('有效期', max_length=200)
    kind = models.CharField('类型', max_length=200)
    asset_num = models.IntegerField('授权数量')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = u'license 历史记录'
        db_table = 'license_history'

    def __unicode__(self):  # __str__ on Python 3
        return self.customer

    @staticmethod
    def autocomplete_search_fields():
        return 'customer'
