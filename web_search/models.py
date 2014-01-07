from django.db import models
from django import forms


# Create your models here.


class ItemForm(forms.Form):
	item_name = forms.CharField(max_length = 200)



class Overview(models.Model):
	
	sem3_id = models.CharField(max_length = 30, primary_key = True,)
	manufacturer = models.CharField(max_length = 30,)
	name = models.CharField(max_length = 10000,)
	model = models.CharField(max_length = 30,)
	cat_id = models.IntegerField()
	lowest_price = models.DecimalField(max_digits = 10, decimal_places = 2)

	def get_cat_id(self):
		
		return self.cat_id

	def __str__(self):
		return self.sem3_id



class Spec_item(models.Model):
	sem3_id = models.OneToOneField(Overview, primary_key = True, )
	features = models.CharField(max_length = 10000)
	weight = models.DecimalField(max_digits = 10, decimal_places = 2)
	color = models.CharField(max_length = 30)
	width = models.DecimalField(max_digits = 10, decimal_places = 2)
	height = models.DecimalField(max_digits = 10, decimal_places = 2)
	length = models.DecimalField(max_digits = 10, decimal_places = 2)

	def __str__(self):
		return ' '.join([self.sem3_id, 
				self.features, 
				self.weight, 
				self.color,
				self.width,
				self.height,
				self.length])


class Offer_detail(models.Model):
	sem3_id = models.ForeignKey(Overview)
	#sku = models.IntegerField()
	url = models.URLField(max_length = 200)
	seller = models.CharField(max_length = 200)
	price = models.DecimalField(max_digits = 10, decimal_places = 2)
	offer_id = models.CharField(max_length = 30, primary_key = True,)

	def __str__(self):
		return self.seller
				




