from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return render(request,'novo_evento.html')
    else:    
        return render(request,'home.html')

   
