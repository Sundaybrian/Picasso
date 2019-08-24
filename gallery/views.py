from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Image,Category,Location

# Create your views here.

def welcome(request):
    return render(request,'welcome.html')

    

def picassoHome(request):
    photos=Image.get_photos()
    context={
        'photos':photos
    }

    return render(request,'all-canvas/picasso_home.html',context)

def search_results(request):

    if 'photo' in request.GET and request.GET['photo']:

        search_term=request.GET.get('photo')
        search_term_id=Category.fetch_category_id(search_term)

        searched_photos=Image.search_by_category(search_term_id)

        context={
        'message':f"{search_term}",
        'photos':searched_photos
        }

        return render(request,'all-canvas/search.html',context)
                
    else :

        context={
        'message':"You haven't searched for any term"
        }
        return render(request,'all-canvas/search.html',context)    

        