from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^adminfiles/', include('adminfiles.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/',include('django_markdown.urls')),
    url(r'^search/', include('haystack.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += url(r'^', include('apps.blog.urls')),
