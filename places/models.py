from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sector(models.Model):
	name = models.CharField(max_length=50)

	class Meta:
		verbose_name = "Sector"
		verbose_name_plural = "Sectors"

	def __str__(self):
		return self.name
    

class Place(models.Model):
	TYPE_CHOICES = (
		('a', 'Apartment'),
		('h', 'House'),
		('w', 'Warehouse'),
		('b', 'Basement'),
	)
	name = models.CharField(max_length=50)
	type_place = models.CharField(choices=TYPE_CHOICES, max_length=1, verbose_name='Type of Place')
	sector = models.ForeignKey(Sector)
	user = models.ForeignKey(User, verbose_name='User Register')

	class Meta:
		verbose_name = "Place"
		verbose_name_plural = "Places"

	def __str__(self):
		return self.name

class Photo(models.Model):
	url = models.URLField()
	comment = models.TextField()
	place = models.ForeignKey(Place)

	class Meta:
		verbose_name = "Photo"
		verbose_name_plural = "Photos"

	def __str__(self):
		return '%s%s' % (self.place, self.id)
    