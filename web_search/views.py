from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from web_search.models import Overview, ItemForm, Spec_item, Offer_detail
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



class show_result(ListView):
	model = Overview
	template_name = 'web_search/result.html'
	context_object_name = 'overview'
	refer_list = []

	def get(self, *args, **kwargs):
		if (not self.request.COOKIES.has_key('refer')):
			self.refer_list = []
		else:
			refer_list = self.request.COOKIES['refer']
			if refer_list == '':
				self.refer_list = []

			
		self.object_list = self.get_queryset()
		allow_empty = self.get_allow_empty()
		if not allow_empty and len(self.object_list) == 0:
			raise Http404(_(u"Empty list and '%(class_name's.allow_empty' is Flase.") % {'class_name':self.__class__.__name__})
		context = self.get_context_data(object_list = self.object_list)
		
		response = self.render_to_response(context)
		if (self.request.COOKIES.has_key('id')):
			print self.request.COOKIES['id']
		else:
			response.set_cookie('id', '1234556')
		
		response.set_cookie('refer', self.refer_list)
		print self.refer_list

		return response

	def get_queryset(self):
		list = []
		#print type(self.refer_list)

		if (self.request.GET):
			form  = ItemForm(self.request.GET)
			if form.is_valid():
				item_name = form.cleaned_data['item_name']
				#print item_name
				code, result_list, result_count = query.make_query(item_name)
			
				for i in range(result_count):
					deal = result_list[i]
					result = query.send_to_database(deal)
					list.append(result)
					self.refer_list = [result]
				return Overview.objects.filter(sem3_id__in = list)
		elif self.refer_list != []: 
			refer = self.request.COOKIES['refer']
			refer_list = Overview.objects.filter(cat_id__in = refer) 
			return Overview.objects.filter(sem3_id__in = refer_list)

	def get_context_data(self, ** kwargs):
		context = super(index, self).get_context_data(**kwargs)

		return context



class index(ListView):

	model = Offer_detail
	template_name = 'web_search/index.html'
	context_object_name = 'offer'
	refer_list = []

	def get_queryset(self):
		list = []
		#print type(self.refer_list)

		if (self.request.GET):
			form  = ItemForm(self.request.GET)
			if form.is_valid():
				item_name = form.cleaned_data['item_name']
				#print item_name
				code, result_list, result_count = query.make_query(item_name)
			
				for i in range(result_count):
					deal = result_list[i]
					result = query.send_to_database(deal)
					list.append(result)
					self.refer_list = [result]
				return Offer_detail.objects.filter(sem3_id__in = list)
		elif self.refer_list != []: 
			refer = self.request.COOKIES['refer']
			refer_list = Overview.objects.filter(cat_id__in = refer) 
			return Offer_detail.objects.filter(sem3_id__in = refer_list)


	def get_context_data(self, ** kwargs):
		context = super(index, self).get_context_data(**kwargs)

		return context

	


def show_overview(request, item_name):
	
	return render(request, 'web_search/overview.html', {'Overview':'hello'})

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




	

