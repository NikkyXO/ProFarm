from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from User.forms import CustomerCreationForm
from django.contrib.auth import login
from django.urls import reverse

# Create your views here.
from django.shortcuts import render

def get_dashboard(request):
    return render(request, 'User/dashboard.html')

def register_user(request):
    if request.method == 'GET':
        return render(
            request, 'User/register.html',
            {"form": CustomerCreationForm}
        )
    elif request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('dashboard'))