from django import forms
from django.contrib.admin import widgets
from django.utils.translation import ugettext_lazy as _

from .models import Place

class PlaceForm(forms.ModelForm):
	class Meta:
		model = Place
		fields = (
			'name',
			'type_place',
			'sector',
		)
