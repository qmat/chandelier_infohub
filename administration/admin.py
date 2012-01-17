# -*- coding: utf-8 -*-
from django.contrib import admin
from administration.models import WebViewPreset

class WebViewPresetAdmin(admin.ModelAdmin):
    list_display = ('name', 'views', 'urls', 'db_created')

admin.site.register(WebViewPreset, WebViewPresetAdmin)

