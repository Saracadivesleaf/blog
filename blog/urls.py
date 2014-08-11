#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
urlpatterns += patterns((''),
    (r'^sblog/', include('sblog.urls')),
)

urlpatterns += patterns((''),
	(r'^satic/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': '/home/leaves/leaves/blog/static'}
	),
)

urlpatterns += patterns((''),
	(r'^comments/', include('django.contrib.comments.urls')
	),
)