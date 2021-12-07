from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import Post
# Create your views here.

def home(request):
    return render(request,"home.html")

def update(request):
    if request.method == 'POST':  
        upload = PostForm(request.POST, request.FILES)  
        if upload.is_valid():  
            upload.save()  
            return HttpResponse("File uploaded successfuly")  
    else:
        form = PostForm()
        return render(request,"update.html",{"form":form})   


def search(request):
   form = SearchForm()
   if request.method == "POST":
      form = SearchForm(request.POST)
      if form.is_valid:
         return HttpResponseRedirect(...) 
   return render(request, 'search.html',{
          'form': form,
   })
    
