from django.conf.urls import patterns, url
from web_search import views

urlpatterns = patterns('',
	url(r'^$', views.index.as_view(), name = 'index'),
	url(r'^result/$', views.show_result.as_view(), name = 'result'), 
	url(r'^(?P<pk>\w+)/offers/$', views.show_offer.as_view(), name = 'offer'),
	url(r'^(?P<pk>\w+)/specs_item/$', views.show_spec_item.as_view(), name = 'spec_item'),
	#url(r'^\w+/$', views.input_item, name = 'input_item'),
) 