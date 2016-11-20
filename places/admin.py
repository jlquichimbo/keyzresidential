from django.contrib import admin
from .models import Sector, Place

# Register your models here.
@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
	list_display = ('id','name', 'type_place', 'sector', 'user')
	list_filter = ('sector',)
	search_fields = ('name',)

