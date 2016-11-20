from django.conf.urls import url
from .import views

urlpatterns = [
	url(r'^reports/', views.reports_view, name='reports'),
	url(r'^$', views.RentList.as_view(), name='list'),
	url(r'^(?P<pk>\d+)$', views.RentDetail.as_view(), name='detail'),
	url(r'^new/$', views.RentCreation.as_view(), name='new'),
	url(r'^edit/(?P<pk>\d+)$', views.RentUpdate.as_view(), name='edit'),
	url(r'^delete/(?P<pk>\d+)$', views.RentDelete.as_view(), name='delete'),
	# Contracts
	url(r'^contracts/$', views.ContractList.as_view(), name='contract_list'),
	url(r'^contract/(?P<pk>\d+)$', views.ContractDetail.as_view(), name='contract_detail'),
	url(r'^contract_new/$', views.ContractCreation.as_view(), name='contract_new'),
	url(r'^contract_edit/(?P<pk>\d+)$', views.ContractUpdate.as_view(), name='contract_edit'),
	url(r'^contract_delete/(?P<pk>\d+)$', views.ContractDelete.as_view(), name='contract_delete'),
]