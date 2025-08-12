from django.shortcuts import render
from datetime import datetime

def homepage(request):
    return render(request,'home.html',{'year':datetime.now().year})
