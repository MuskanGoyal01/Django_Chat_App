from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages

from .forms import SignUpForm


# Create your views here.
def home(request):
    return render(request, 'chat/home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            messages.success(request, 'Signed up successfully!')

            return redirect('home')

    else:
        form = SignUpForm()

    return render(request, 'chat/signup.html', {'form': form})

