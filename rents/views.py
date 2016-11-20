from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from datetime import date

# Crud Django:
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
# KeysResidential
from .models import Rent, Contract
from .forms import RentForm, ContractForm

# Create your views here.
def authentication(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/rents/reports')
		else:
			error_message='Credenciales invalidas'
			context = {
				'error_message': error_message,
			}

			return render(request, 'login.html', context)
	else:
		return render(request, 'login.html', {})

@login_required()
def reports_view(request):
	template = 'rents/reports.html'
	context = {
		'page_title': 'Management',
	}
	return render(request, template, context)

# CRUD CONTRACTS
class ContractList(ListView):
	model = Contract

	def get_context_data(self, **kwargs):
		context = super(ContractList, self).get_context_data(**kwargs)
		context.update({
				'page_title': 'Contracts'
			})
		return context

@method_decorator(login_required, name='dispatch')
class ContractDetail(DetailView):
	model = Contract


class ContractCreation(CreateView):
	model = Contract
	form_class = ContractForm
	success_url = reverse_lazy('rents:contract_list')

	def get_context_data(self, **kwargs):
		context = super(ContractCreation, self).get_context_data(**kwargs)
		context.update({
			'page_title':'New Contract',
			})
		return context

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			ContractForm = form.save(commit=False)
			ContractForm.date = date.today()
			ContractForm.save()
			context = {
				'page_title': 'Contracts'
			}
			return redirect('/rents/contracts/')

class ContractUpdate(UpdateView):
	model = Contract
	form_class = ContractForm
	success_url = reverse_lazy('rents:contract_list')

class ContractDelete(DeleteView):
	model = Contract
	success_url = reverse_lazy('rents:contract_list')


# RENTS
class RentList(ListView):
	model = Rent

	def get_context_data(self, **kwargs):
		context = super(RentList, self).get_context_data(**kwargs)
		context.update({
				'page_title': 'Rents'
			})
		return context

@method_decorator(login_required, name='dispatch')
class RentDetail(DetailView):
	model = Rent


class RentCreation(CreateView):
	model = Rent
	form_class = RentForm
	success_url = reverse_lazy('rents:Rent_list')

	def get_context_data(self, **kwargs):
		context = super(RentCreation, self).get_context_data(**kwargs)
		context.update({
			'page_title':'New Rent',
			})
		return context

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			RentForm = form.save(commit=False)
			RentForm.collector = request.user
			RentForm.save()
			context = {
				'page_title': 'Rents'
			}
			return redirect('/rents/')

class RentUpdate(UpdateView):
	model = Rent
	form_class = RentForm
	success_url = reverse_lazy('rents:list')

class RentDelete(DeleteView):
	model = Rent
	success_url = reverse_lazy('rents:list')
