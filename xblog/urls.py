from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/',include('django_markdown.urls')),
    url(r'^search/', include('haystack.urls')),
)

urlpatterns += url(r'^', include('apps.blog.urls')),
