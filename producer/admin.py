# -*- coding: utf-8 -*-
import random
from django.contrib import admin
from .models import FunctionMapping, LicenseHistory
import commands
import os
from django.template.response import TemplateResponse
from django.contrib.admin import helpers
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.utils import get_deleted_objects, model_ngettext


class MyAdminSite(admin.AdminSite):
    site_header = u'license producer'  # 此处设置页面显示标题
    site_title = u'灵犀联云'  # 此处设置页面头部标题


admin_site = MyAdminSite(name='management')


class FunctionMappingAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'function', 'name')
    ordering = ['serial_number']
    list_per_page = 10

    actions = ['make_published']
    action_form = helpers.ActionForm

    def make_published(self, request, queryset):
        if request.POST.get('post'):
            function_list = []
            function_names = []
            for func in queryset:
                function_list.append(func.serial_number)
                function_names.append(func.name)
            print function_list, function_names
            self.message_user(request, u"请稍后，正在生成license，包含(%s)" % ','.join(function_names))

            customer = '百度'
            kind = 2
            effective_time = 3
            asset_num = random.randrange(0, 99999)
            lh = LicenseHistory(customer=customer, kind=kind, effective_time=effective_time,
                                function=','.join(function_names), asset_num=asset_num)
            lh.save()

    make_published.short_description = u"选中上述模块生成license"


class LicenseHistoryAdmin(admin.ModelAdmin):
    list_display = ('customer', 'function', 'asset_num', 'effective_time', 'kind', 'create_time')
    ordering = ['create_time', 'asset_num']
    search_fields = ('customer', 'kind')
    list_per_page = 10

    actions = ['make_published']
    action_form = helpers.ActionForm


admin_site.register(FunctionMapping, FunctionMappingAdmin)
admin_site.register(LicenseHistory, LicenseHistoryAdmin)
