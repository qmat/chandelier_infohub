# -*- coding: utf-8 -*-
from django.contrib import admin
from quartz.models import QuartzSketch

class QuartzSketchAdmin(admin.ModelAdmin):
    list_display = ('name', 'file', 'db_created')

admin.site.register(QuartzSketch, QuartzSketchAdmin)

