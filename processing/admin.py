# -*- coding: utf-8 -*-
from django.contrib import admin
from processing.models import ProcessingSketch

class ProcessingSketchAdmin(admin.ModelAdmin):
    list_display = ('text', 'db_created')

admin.site.register(ProcessingSketch, ProcessingSketchAdmin)

