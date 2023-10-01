from msilib.schema import Error
from multiprocessing import context
from django import forms
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Detailsm
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'This email is already registerd! Please register with different Mail')
                form=UserRegisterForm()
                return render(request, 'register.html', {'form': form})
            else:
                form.save()
                messages.success(request, f'Your account is created! You can login now!')
                return redirect('login')

    else:
        form=UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def home(request):
    details=Detailsm.objects.all()
    puser=request.user
    for detail in details:
        if detail.user==puser:
            context={'data':detail}
            return render(request,'home.html',context)
    context={'data':{'name':'---','age':'---','dob':'---','country_code':'---','contact':'---','mail':'---',
                     'address':'---','postal':'---','city':'---','state':'---','country':'---',}}
    return render(request,'home.html',context)


class DetailsmCreateView(LoginRequiredMixin,CreateView):
    model=Detailsm
    fields=['name','age','dob','country_code','contact','mail','address','postal','city','state','country']

    def form_valid(self, form):
        puser=self.request.user
        details=Detailsm.objects.all()
        for detail in details:
            if detail.user==puser:
                detail.delete()
        form.instance.user=puser
        form.save()
        return redirect('home')
  
    
    