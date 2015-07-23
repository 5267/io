from django.conf.urls import url
from . import views

urlpatterns = (
        url(r'^article/(?P<slug>\S+)/$', views.ArticleDetail.as_view(), name='article'),
        url(r'^archives/', views.Archives, name='archives'),
        url(r'^tag/(?P<slug>[-\w]+)/$', views.ArticlesOfTag, name='tag'),
        url(r'^category/(?P<slug>[-\w]+)/$', views.ArticlesOfCategory, name='category'),
        url(r'^', views.Home, name='home'),
)
