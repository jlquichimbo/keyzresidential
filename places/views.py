from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Crud Django:
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
# KeysResidential
from .models import Place
from .forms import PlaceForm

# Create your views here.
def index(request):
	template = 'index.html'
	context = {
	
	}
	return render(request, template, context)

class PlaceList(ListView):
	model = Place

	def get_context_data(self, **kwargs):
		context = super(PlaceList, self).get_context_data(**kwargs)
		context.update({
				'page_title': 'Places'
			})
		return context

@method_decorator(login_required, name='dispatch')
class PlaceDetail(DetailView):
	model = Place


class PlaceCreation(CreateView):
	model = Place
	form_class = PlaceForm
	success_url = reverse_lazy('rents:place_list')

	def get_context_data(self, **kwargs):
		context = super(PlaceCreation, self).get_context_data(**kwargs)
		context.update({
			'page_title':'New Place',
			})
		return context

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			placeForm = form.save(commit=False)
			placeForm.user = request.user
			placeForm.save()
			context = {
				'page_title': 'Places'
			}
			return redirect('/places/')

class PlaceUpdate(UpdateView):
	model = Place
	form_class = PlaceForm
	success_url = reverse_lazy('places:list')

class PlaceDelete(DeleteView):
	model = Place
	success_url = reverse_lazy('places:list')
