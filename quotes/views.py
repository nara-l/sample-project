# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import TemplateView, CreateView
from api import DataAPI
from datetime import datetime
import dateutil.parser

from quotes.models import Comments


class IndexPage(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(IndexPage, self).get_context_data(**kwargs)
        content_api = DataAPI()
        context['first_article'] = content_api.get_article_with_tag('10-promise')
        context['random_articles'] = content_api.get_random_articles()
        context['title'] = context['first_article']['headline']
        print context['title']
        return context


class Article(TemplateView):
    template_name = 'article_details.html'

    def get_context_data(self, **kwargs):
        context = super(Article, self).get_context_data(**kwargs)

        content_api = DataAPI()
        context['article'] = content_api.get_article_by_slug(self.kwargs['slug'])
        context['quotes'] = content_api.quotes_api()[0:3]
        context['title'] = context['article']['headline']
        context['comments'] = Comments.objects.filter(slug=context['article']['slug'])
        context['related_articles'] = content_api.get_random_articles(num_articles=5)
        return context


class CreateComment(CreateView):
    model = Comments
    fields = ['username', 'comment', 'slug']

    def form_valid(self, form):
        comment = form.save()
        if not comment.username:
            comment.username = 'Anonymous'
            comment.save()
        return HttpResponse(json.dumps({
            'success': True,
            'html': render_to_string('parts/comment.html', {'comment': comment})}),
            content_type='application/json')
