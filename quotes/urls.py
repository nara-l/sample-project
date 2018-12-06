from django.conf.urls import url
from .views import IndexPage, Article, CreateComment

urlpatterns = [
    url(r'^$', IndexPage.as_view(template_name='index.html'), name='index'),
    url(r'^article/(?P<slug>[-\w]+)/$', Article.as_view(), name='article_detail'),
    url(r'^article/(?P<slug>[-\w]+)/comment$', CreateComment.as_view(), name='create_comment')
]