from django.shortcuts import render

from .models import PostModel

# Create your views here.
def personal_view(request):
    personal_posts = PostModel.objects.all().filter(topic="personal")
    return render(request, 'personal/personal.html', {'personal_posts': personal_posts})


def personal_content(request, title):
    content = PostModel.objects.get(title__contains=title)
    return render(request, 'personal/personal_content.html', {'content': content})


def spirituality_view(request):
    spirituality_posts = PostModel.objects.all().filter(topic="spirituality")
    return render(request, 'spirituality/spirituality.html', {'spirituality_posts': spirituality_posts})


def spirituality_content(request, title):
    content = PostModel.objects.get(title__contains=title)
    return render(request, 'spirituality/spirituality_content.html', {'content': content})

