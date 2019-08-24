from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import Image

# Create your views here.

def welcome(request):
    return render(request,'welcome.html')

    

def picassoHome(request):
    photos=Image.get_photos()
    context={
        'photos':photos
    }

    return render(request,'all-canvas/picasso_home.html',context)