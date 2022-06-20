from itertools import product
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from main.forms import ProductForm
from main.models import Product

# Create your views here.
from .models import *
from .forms import CreateUserForm

def index(request):
    return render(request, 'accounts/login.html')

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('dashboard')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'accounts/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('dashboard')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('dashboard')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login') 


@login_required(login_url='login')
def dashboard(request):
	products = Product.objects.all()

	context = {'products':products}
	return render(request, 'accounts/dashboard.html', context)



@login_required(login_url='login')
def createProduct(request):
	form = ProductForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('dashboard')

	context = {'form':form}
	return render(request, 'accounts/product_form.html', context)

@login_required(login_url='login')
def updateProduct(request, pk):

	product = Product.objects.get(id=pk)
	form = ProductForm(instance=product)

	if request.method == 'POST':
		form = ProductForm(request.POST, instance=product)
		if form.is_valid():
			form.save()
			return redirect('dashboard')

	context = {'form':form}
	return render(request, 'accounts/update_product.html', context)

@login_required(login_url='login')
def deleteProduct(request, pk):
	product = Product.objects.get(id=pk)
	if request.method == "POST":
		product.delete()
		return redirect('dashboard')

	context = {'item':product}
	return render(request, 'accounts/delete.html', context)


@login_required(login_url='login')
def products(request):
	products = Product.objects.all()

	return render(request, 'accounts/products.html', {'products':products})