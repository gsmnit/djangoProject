from django.shortcuts import render
from .models import Post



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "blog-template/home.html", context)


def about(request):
    return render(request, "blog-template/about.html" ,{'title': "about"})

###  djangoProject -> template -> blog -> HTMLFILES