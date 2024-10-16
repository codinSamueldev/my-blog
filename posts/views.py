from django.shortcuts import render

from .models import PostModel

# Create your views here.
def personal_view(request):
    personal_posts = PostModel.objects.all().filter(topic="personal")
    return render(request, 'personal/personal.html', {'personal_posts': personal_posts})


def spirituality_view(request):
    spirituality_posts = PostModel.objects.all().filter(topic="spirituality")
    return render(request, 'spirituality/spirituality.html', {'spirituality_posts': spirituality_posts})


def personalspiritual_content(request, title, template_name):
    content = PostModel.objects.get(title__contains=title)
    return render(request, template_name, {'content': content})
