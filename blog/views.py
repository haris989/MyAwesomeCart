from django.shortcuts import render
from .models import Blogpost
# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'blog/index.html')

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'blog/blogpost.html',
                  {'post':post})
