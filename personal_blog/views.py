from django.shortcuts import render

from posts.models import PostModel


def home(request):
    posts = PostModel.objects.all()[:3]
    return render(request, 'home.html', {'posts': posts})

