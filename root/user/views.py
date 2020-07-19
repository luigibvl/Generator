from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import form_delete_account



def home(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


@login_required
def delete_account(request):
    if request.method == 'POST':
        form = form_delete_account(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            if username == request.user.username:
                u = User.objects.get(username = username)
                u.delete()
                return redirect('home')
    else:
        form = form_delete_account()
    return render(request, 'registration/delete_account.html',{
        'form': form
    })
