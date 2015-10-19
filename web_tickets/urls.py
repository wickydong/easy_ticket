from django.conf.urls import patterns, include, url
from django.contrib import admin
from web_tickets.views import index,login_form

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tickets.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^$', index),
    url('^login_form/$', login_form),
)
