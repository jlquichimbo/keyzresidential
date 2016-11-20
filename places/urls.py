from django.conf.urls import url
from .import views

urlpatterns = [
	url(r'^index/', views.index, name='index'),
	url(r'^$', views.PlaceList.as_view(), name='list'),
	url(r'^(?P<pk>\d+)$', views.PlaceDetail.as_view(), name='detail'),
	url(r'^new/$', views.PlaceCreation.as_view(), name='new'),
	url(r'^edit(?P<pk>\d+)$', views.PlaceUpdate.as_view(), name='edit'),
	url(r'^delete/(?P<pk>\d+)$', views.PlaceDelete.as_view(), name='delete'),
]