from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Contract, Rent, RentDeduction
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ('id', 'username', 'first_name', 'last_name', 'is_staff', 'is_active')
	list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

# UserAdmin.list_display = ('id', 'username', 'first_name', 'last_name', 'is_staff', 'is_active')
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

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

