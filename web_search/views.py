from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from web_search.models import Overview, ItemForm, Spec_item
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic import list_detail

import exe_query as query


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

def show_spec_item(request, item_name):
	spec = get_object_or_404(Spec_item, sem3_id__iexact = item_name)

	return list_detail.object_list(
		request,
		queryset = Spec_item.objects.get(sem3_id  = spec), )


