from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime
import requests, json
    
# Create your views here.
def index(request, context):
    
    return render(request,'main_app/index.html',context)
    