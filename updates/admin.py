# -*- coding: utf-8 -*-
from django.contrib import admin
from updates.models import Update

class UpdateAdmin(admin.ModelAdmin):
    list_display = ('source', 'author', 'text', 'timestamp', 'db_created')

admin.site.register(Update, UpdateAdmin)

