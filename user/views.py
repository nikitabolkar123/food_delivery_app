from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from user.forms import Signupform


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login.html')
    else:
        form = Signupform()

    return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('next')
        else:
            messages.error(request, 'Invalid username or password')  # Display an error message
    return render(request, 'login.html')


def Next(request):
    return render(request, 'next.html')
