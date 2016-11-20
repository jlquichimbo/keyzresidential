from django.db import models
from django.contrib.auth.models import User
from places.models import Place

# Create your models here.
class Contract(models.Model):
	tenant = models.ForeignKey(User, on_delete = models.PROTECT, limit_choices_to =  {'groups__name': 'tenant'})
	place = models.ForeignKey(Place, on_delete = models.CASCADE)
	amount = models.DecimalField(max_digits=5, decimal_places=2)
	date = models.DateField()

	class Meta:
		verbose_name = "Contract"
		verbose_name_plural = "Contracts"

	def __str__(self):
		return '%s, %s - %s' % (self.place, self.tenant, self.amount)

class Rent(models.Model):
	month = models.DateField()
	section8_amount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Section 8 Amount')
	tenant_amount_due = models.DecimalField(max_digits=5, decimal_places=2)
	sec_deposit_due = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Security Deposit Due', default=0)
	misc_add_fees = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Miscellaneous Aditional Fees', default=0)
	backrent_amount_due = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	tenant_total_amount_due = models.DecimalField(max_digits=5, decimal_places=2)
	total_paid = models.DecimalField(max_digits=5, decimal_places=2)
	month_balance = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	collector = models.ForeignKey(User, limit_choices_to =  {'groups__name': 'collector'})
	contract = models.ForeignKey(Contract)



	class Meta:
		verbose_name = "Rent"
		verbose_name_plural = "Rents"

	def __str__(self):
		return '%s - %s' % (self.contract, self.month)

class RentDeduction(models.Model):
	rent = models.ForeignKey(Rent)
	date = models.DateField()
	payment = models.DecimalField(max_digits=5, decimal_places=2)

	class Meta:
		verbose_name = "RentDeduction"
		verbose_name_plural = "RentDeductions"

	def __str__(self):
		return '%s - %s' % (self.rent, self.payment)
    	