from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.

@login_required
def vc(request):
    return render(request, 'videocall/home.html')

@login_required
def stream(request):

    return render(request, 'videocall/stream.html')
