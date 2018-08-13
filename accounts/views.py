
#Creating a sign up page:

from django.shortcuts import render
from django.contrib.auth import login, authenticate                     #import all the necessary packages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():               #validation
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home/index.html')
    else:
        form = UserCreationForm()           #form is created
    return render(request, 'accounts/signup.html', {'form': form})