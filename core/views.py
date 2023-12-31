from django.shortcuts import render, redirect
from item.models import Category, Item
from django.contrib.auth import logout
from django.contrib import messages
from .forms import SignUpForm

def index(request):
    items = Item.objects.filter(is_sold=False).order_by('-created_at')
    categories = Category.objects.all()

    category_id = request.GET.get('category', 0)
    if category_id:
        items = Item.objects.filter(category_id=category_id)
    
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

def logout_user(request):
    logout(request)
    return redirect('core:index')