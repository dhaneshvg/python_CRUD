from django.shortcuts import render, redirect

from .forms import ModelForm
from .models import product


# Create your views here.

def home(request):
    prod = product.objects.all()
    return render(request, 'index.html', {'products': prod})


def retrive(request, prod_id):
    prod_detail = product.objects.get(id=prod_id)
    return render(request, 'retrive.html', {'prod_detail': prod_detail})


def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        price = request.POST.get('price')
        img = request.POST.get('img')
        shop = product(name=name, desc=desc, price=price, img=img)
        shop.save()
        print('product added')
    return render(request, 'create.html')


def update(request, prod_id):
    obj = product.objects.get(id=prod_id)
    form = ModelForm(request.POST or None, request.FILES, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form, 'obj': obj})


def delete(request, prod_id):
    if request.method == "POST":
        prod_del = product.objects.get(id=prod_id)
        prod_del.delete()
        return redirect('/')
    return render(request, 'delete.html')
