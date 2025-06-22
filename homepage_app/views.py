from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render (request, 'homepage_app/index.html', context = {})

