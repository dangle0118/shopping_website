from django.conf.urls import patterns, url
from web_search import views

urlpatterns = patterns('',
	url(r'^$', views.index, name = 'index'),
	url(r'^(?P<item_name>\w+)/overview/$', views.show_overview, name = 'overview'),
	url(r'^(?P<item_name>\w+)/specs_item/$', views.show_spec_item, name = 'spec_item'),
	#url(r'^\w+/$', views.input_item, name = 'input_item'),
) 