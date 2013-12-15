from django.db import models
from django import forms


# Create your models here.


class ItemForm(forms.Form):
	item_name = forms.CharField(max_length = 200)



class Overview(models.Model):
	
	sem3_id = models.CharField(max_length = 30, primary_key = True,)
	manufacturer = models.CharField(max_length = 30,)
	name = models.CharField(max_length = 500,)
	model = models.CharField(max_length = 30,)
	cat_id = models.IntegerField()

	def __str__(self):
		return ' '.join([self.sem3_id, self.manufacturer, self.name, self.model, self.cat_id])



class Spec_item(models.Model):
	sem3_id = models.CharField(max_length = 30, primary_key = True,)
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

#class item(models.Model):
#	url = models.URLField(max_length = 200)
#	seller = models.CharField(max_length = 30)




