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