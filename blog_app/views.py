from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blogpost
from .forms import BlogpostForm

def blog(request):
    if request.method == "POST":
        form = BlogpostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('blog')
                        
        else:
            return HttpResponse("Failed to post")
    
     
    data = Blogpost.objects.all().order_by('-id') 
    return render (request, 'blog_app/blog.html', {'data' : data})
    