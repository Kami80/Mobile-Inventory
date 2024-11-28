from django.shortcuts import render, get_object_or_404, redirect
from .models import Mobile, Brand
from .forms import MobileForm, BrandForm

def index(request):
    mobiles = Mobile.objects.all()
    return render(request, 'inventory/index.html', {'mobiles': mobiles})

def add_mobile(request):
    if request.method == 'POST':
        form = MobileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MobileForm()
    return render(request, 'inventory/add_mobile.html', {'form': form})

def edit_mobile(request, pk):
    mobile = get_object_or_404(Mobile, pk=pk)
    if request.method == 'POST':
        form = MobileForm(request.POST, instance=mobile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MobileForm(instance=mobile)
    return render(request, 'inventory/edit_mobile.html', {'form': form})

def add_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the index or another appropriate page
    else:
        form = BrandForm()
    return render(request, 'inventory/add_brand.html', {'form': form})

def delete_mobile(request, pk):
    mobile = get_object_or_404(Mobile, pk=pk)
    mobile.delete()
    return redirect('index')
