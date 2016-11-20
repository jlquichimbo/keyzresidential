from django import forms
from django.contrib.admin import widgets
from django.utils.translation import ugettext_lazy as _

from .models import Rent, Contract

class RentForm(forms.ModelForm):
	class Meta:
		model = Rent
		fields = (
			'contract',
			'month',
			'section8_amount',
			'tenant_amount_due',
			'sec_deposit_due',
			'misc_add_fees',
			'backrent_amount_due',
			'tenant_total_amount_due',
			'total_paid',
			'month_balance',
			'month_balance',
		)
		widgets = {
			'month': forms.SelectDateWidget(),
		}

class ContractForm(forms.ModelForm):
	class Meta:
		model = Contract
		fields = (
			'tenant',
			'amount',
			'place',
			)
