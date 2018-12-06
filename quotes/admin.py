# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from quotes.models import Comments


# Register your models here.


class CommentsAdmin(admin.ModelAdmin):
    readonly_fields = ('comment', 'slug')


admin.site.register(Comments, CommentsAdmin)
