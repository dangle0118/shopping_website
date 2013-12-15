from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo_website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^search/', include('web_search.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
)
