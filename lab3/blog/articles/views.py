from django.shortcuts import render
from .models import Article

def archive(request):
    posts = Article.objects.all()  # Получаем все статьи
    return render(request, 'archive.html', {"posts": posts})