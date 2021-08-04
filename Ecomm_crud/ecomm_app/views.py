from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ecomm_form
from .models import ecomm_model
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm = ecomm_form(request.POST)
            if fm.is_valid():
                nm = fm.cleaned_data['name']
                ph = fm.cleaned_data['phone']
                eml = fm.cleaned_data['email']
                prod = fm.cleaned_data['product']
                qt = fm.cleaned_data['quantity']

                obj = ecomm_model(name=nm,phone=ph,email=eml,product=prod,quantity=qt)
                obj.save()
        else:
            fm = ecomm_form()
        dt = ecomm_model.objects.all
        return render(request,'ecomm/home.html',{'form':fm,'details':dt})
    else:
        return HttpResponseRedirect('/login')
'''
def update(request,id):
    if request.method=='POST':
        md = ecomm_model.objects.get(pk=id)
        fm = ecomm_form(request.POST, instance=md)
        if fm.is_valid():
            fm.save()
    else:
        md = ecomm_model.objects.get(pk=id)
        fm = ecomm_form(instance=md)
    return render(request,'update.html',)'''

def delete(request,id):
    stu = ecomm_model.objects.get(pk=id)
    stu.delete()
    return redirect('/ecomm/home')
def update(request,id):
    if request.method == 'POST':
        stu = ecomm_model.objects.get(pk=id)
        form = ecomm_form(request.POST, instance=stu)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'successfully updated!')
            return HttpResponseRedirect('/ecomm/home')
    else:
        stu = ecomm_model.objects.get(pk=id)
        form = ecomm_form(instance=stu)
    return render(request, 'ecomm/update.html', {'form': form})
def success(request):
    return render(request,'ecomm/success.html')

