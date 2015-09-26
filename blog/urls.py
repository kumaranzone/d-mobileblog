from django.conf.urls import patterns, url
from . import views, feed
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = patterns(
    '',
    url(r'^feed/$', feed.LatestPosts(), name="feed"),
    url(r'^$', views.BlogIndex.as_view(), name="index"),
    url(r'^entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),    
)


