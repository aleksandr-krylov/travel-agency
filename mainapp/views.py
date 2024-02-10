from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News


# Create your views here.
def home(request):
    # Pull up 4 latest news to display on the home page
    top3news = News.objects.all()[:3]

    return render(
        request,
        'mainapp/home.html',
        {'topnews': top3news}
    )


def about(request):
    return render(request, 'mainapp/about.html', {'title': 'О нас'})


def contacts(request):
    return render(request, 'mainapp/contacts.html', {'title': 'Контакты'})


def news(request):
    news = News.objects.all()
    top3news = news[:3]
    context = {
        'news': news,
        'top3news': top3news,
        'title': 'Новости'
    }
    
    return render(request, 'mainapp/news.html', context)


def newspost(request, pk):
    post = News.objects.get(id=pk)
    top3news = News.objects.all()[:3]
    context = {
        'post': post,
        'top3news': top3news,
        'title': f'Новость {pk}'
    }

    return render(request, 'mainapp/news-post.html', context)


def services(request):
    return render(request, 'mainapp/services.html')
