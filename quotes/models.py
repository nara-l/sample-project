# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Comments(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True, default='Anonymous')
    comment = models.TextField()
    slug = models.SlugField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{username} commented on {slug}'.format(username=self.username, slug=self.slug)
