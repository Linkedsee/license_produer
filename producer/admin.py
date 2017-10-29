# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import FunctionMapping
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
        print request, queryset
        function_list = []
        for func in queryset:
            function_list.append(func.serial_number)
        print function_list
        self.message_user(request, u"请稍后")
        pass

    make_published.short_description = u"选中上述模块生成license"


admin_site.register(FunctionMapping, FunctionMappingAdmin)