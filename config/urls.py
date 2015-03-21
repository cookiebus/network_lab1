from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zhijiang.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'home.index'),
    url(r'^new/(\d+)', 'news.views.next_new'),
    url(r'^spider/', 'news.views.spider'),
    url(r'^admin/', include(admin.site.urls)),
)
