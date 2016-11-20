from django.contrib import admin
from .models import Contract, Rent, RentDeduction

# Register your models here.
class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'place', 'tenant', 'amount', 'date')

admin.site.register(Contract, ContractAdmin)

class RentAdmin(admin.ModelAdmin):
	list_display = (
		'id', 
		'contract', 
		'month', 
		'collector', 
		'section8_amount', 
		'tenant_amount_due', 
		'tenant_total_amount_due', 
		'total_paid', 
		'month_balance',
		)
	list_filter = ('contract',  'month', 'collector')
	search_fields = ('month',)

admin.site.register(Rent, RentAdmin)

class RentDeductionAdmin(admin.ModelAdmin):
	list_display = ('id', 'rent', 'date', 'payment')
	list_filter = ('rent','date')

admin.site.register(RentDeduction, RentDeductionAdmin)