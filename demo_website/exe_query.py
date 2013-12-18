import os
from semantics3 import Products
from web_search.models import Overview, Spec_item
import json




def send_to_database(deal):
	if deal.has_key('model'):
		model_id = deal['model']
	else:
		model_id = 'none'
	if deal.has_key('color'):
		color_id = deal['color']
	else:
		color_id = 'none'
	if deal.has_key('manufacturer'):
		manufacturer_id = deal['manufacturer']
	elif deal.has_key('brand'):
		manufacturer_id = deal['brand']

	if deal.has_key('height'):
		height_id = deal['height']
	else:
		height_id = 0
	if deal.has_key('weight'):
		weight_id = deal['weight']
	else:
		weight_id = 0
	if deal.has_key('width'):
		width_id = deal['width']
	else:
		width_id = 0
	if deal.has_key('length'):
		length_id = deal['length']
	else:
		length_id = 0
	


	temp = Overview(sem3_id = deal['sem3_id'],
		 manufacturer = manufacturer_id,
		 name = deal['name'],
		 model = model_id,
		 cat_id = deal['cat_id']
		 )
	temp.save()


	features = json.dumps(deal['features'])
	
	temp = Spec_item(sem3_id = deal['sem3_id'],
		features = deal['features'],
		color = color_id,
		weight = weight_id,
		length = length_id,
		width = width_id,
		height = height_id
		)
	temp.save()

# should return offer details
	return {'name':deal['name'], 'sem3_id': deal['sem3_id']}


	#sitedetail = deal['sitedetails']

	#for temp in sitedetail:
	#	url = temp['url']
	#	seller = temp['name']
	#	latestoffers = temp['latestoffers']
	#	for offer in latestoffers:
	#		Item_add










def make_query(item_name):
	products = Products(
		api_key = 'SEM3A92F1C506BB40F217AA3716D7C9A8815', 
		api_secret = 'ZGU0MWJiNjY1ZTY1OTgxZDVhODFiYWNkYzNkOTBjZjA')

	products.products_field('name', 'Samsung')
	result_query = products.get_products()
	code = result_query['code']
	result_list = result_query['results']
	result_count = result_query['results_count']

	return code, result_list, result_count

#	for i in range(result_count):
#		deal = result_list[i]
# deals are decoded here, pass to front end/templates

#store to our database
#		send_to_database(deal)





