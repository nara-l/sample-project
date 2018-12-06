import json
import random
import os
import dateutil.parser

from datetime import datetime
from django.conf import settings
from django.utils.text import slugify


class DataAPI():

    def content_api(self):
            with open(os.path.join(settings.PROJECT_ROOT, 'content_src/content_api.json'), 'r') as jsonfile:
                response = json.load(jsonfile)
                return response

    def quotes_api(self):
        with open(os.path.join(settings.PROJECT_ROOT, 'content_src/quotes_api.json'), 'r') as jsonfile:
            response = json.load(jsonfile)
            return response

    def normalize_article(self, res):
        article = {}
        article['image'] = res['images'][0]['image']
        article['image_name'] = res['images'][0]['name']
        article['body'] = res['body']
        article['headline'] = res['headline']
        parsed_date = dateutil.parser.parse(res['publish_at'])
        date = datetime.strftime(parsed_date, '%B, %d %Y')
        article['published_date'] = date
        article['link'] = res['instruments'][0]['links']['content']
        article['author'] = res['authors'][0]['byline']
        article['slug'] = slugify(article['headline'])
        article['disclosure'] = res['disclosure']
        return article

    def get_article_with_tag(self, slug):
        response = self.content_api()
        for res in response['results']:

            if self.has_tag(res, slug):
                return self.normalize_article(res)
        return None

    def get_article_by_slug(self, slug):
        items = self.content_api()
        for item in items['results']:

            if slugify(item['headline']) == slug:
                return self.normalize_article(item)

    def has_tag(self, item, slug):
        slugs = [x['slug'] for x in item['tags']]
        return slug in slugs

    def get_random_articles(self, num_articles):
        response = self.content_api()
        items = []
        while len(items) < num_articles:
            chosen = random.choice(response['results'])
            not_in_items = chosen['headline'] not in [x['headline'] for x in items]
            if not_in_items:
                items.append(self.normalize_article(chosen))
        return items





