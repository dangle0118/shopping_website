from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from web_search.models import Overview, ItemForm, Spec_item
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic import DetailView
import exe_query as query
import json


# Create your views here.

def input_item(request):
	temp = request.GET
	return HttpResponse('will be showing item ' + temp['item_name'])


def search_item(request):
	if request.method == 'GET':
		form = ItemForm(request.GET)
		if form.is_valid():
			return render(request, 'web_search/specs_item.html',{'form': form,}) 
		else:
			form = ItemForm()
		return render(request, 'web_search/index.html', {'form': form,})


def index(request):

	if request.method == 'GET':
		form = ItemForm(request.GET)
		if form.is_valid():
			item_name = form.cleaned_data['item_name']
			
			code, result_list, result_count = query.make_query(item_name)

			list = []
			for i in range(result_count):
				deal = result_list[i]
				result = query.send_to_database(deal)

				list.append(result)



			return render(request, 'web_search/index.html',{'result_item': list}) 
		else:
			form = ItemForm()
		return render(request, 'web_search/index.html', {'form': form,})


def show_overview(request, item_name):
	try:
		search = Overview.objects.get(pk = item_name)
	except Overview.DoesNotExist:
		raise Http404
	return render(request, 'web_search/overview.html', {'Overview':seach})

class show_spec_item(DetailView):
	model = Spec_item
	template_name = 'web_search/specs_item.html'
	context_object_name = 'specs_item'

	def get_context_data(self, **kwargs):
		context = super(show_spec_item, self).get_context_data(**kwargs)


		features = get_object_or_404(Spec_item, sem3_id = self.kwargs[self.pk_url_kwarg])
		temp = (json.loads(features.features))
		list = []
		for a in temp:
			list.append(temp[a])

		context['features'] = list
		return context



	

