from django.shortcuts import render

from .notes import notes
def homepage(req):
    note=Note.objects.all().order_by('-id');
    return render(request,"home.html",{"notes":notes})
