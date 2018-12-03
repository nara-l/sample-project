# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic.base import TemplateView

class IndexPage(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(IndexPage, self).get_context_data(**kwargs)
        context['title'] = "Hello to the quotes app world"
        return context

