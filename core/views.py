from django.shortcuts import render, redirect
from item.models import  Category, Item
from django.contrib.auth import logout
from django.contrib import messages

from .forms import SignupForm




def index(request):
    items = Item.objects.filter(is_sold=False)
    category = Category.objects.all()
    listt = {
        'category' : category,
        "items" :     items,
        
    }
    return render(request, 'core/index.html', listt)


def contact(request):
    return render(request, "core/contact.html")


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        
        if form.is_valid():

            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    a = {
        'form' : form
    }
    return render(request, 'core/signup.html',a)


def logout_user(request ):
    logout(request)
    messages.success(request, ("Loggedout succefully !"))
    return redirect('core:index')