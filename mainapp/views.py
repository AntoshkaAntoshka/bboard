from django.shortcuts import render
from .models import Bb

def index(request):
    bbs = Bb.objects.order_by('-published')
    return render(request, 'mainapp/index.html', {'bbs': bbs})