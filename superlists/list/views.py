from django.shortcuts import render,redirect
from django.http.response import HttpResponse
# Create your views here.


def home_page(request):
    html = "<html><title>To-Do</title></html>"

    return render(request ,'index.html',{'hi': 3})