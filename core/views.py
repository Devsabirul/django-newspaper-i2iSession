from django.shortcuts import render
from .models import *

from itertools import islice


def home(request):
    is_logged_in = False
    if request.user.is_authenticated:
        is_logged_in = True
    flash_news = FlashNews.objects.all()
    totalnews = News.objects.all().count()
    totalsport = News.objects.filter(category="SPORT").count()
    totalpolitics = News.objects.filter(category="POLITICS").count()
    totalbusiness = News.objects.filter(category="BUSINESS").count()
    totalarts = News.objects.filter(category="ARTS").count()

    news = News.objects.all().order_by("-id")
    recentpost = News.objects.all().order_by("-id")
    sport_news = News.objects.filter(category="SPORT").order_by("-id")
    newssport_ = News.objects.filter(category="SPORT")
    celebrity = News.objects.filter(category="CELEBRITY").order_by("-id")
    # Get Unique Category
    uCategory = dict()
    for unique in news:
        if unique.category in uCategory:
            uCategory[unique.category] += 1
        else:
            uCategory[unique.category] = 1

    context = {
        'is_logged_in': is_logged_in,
        'flash_news': flash_news,
        'news': news,
        'sport_news': sport_news,
        'newssport_': newssport_,
        'uCategory': uCategory,
        'celebrity': celebrity,
        'recentpost': recentpost,
        'totalnews': totalnews,
        'totalsport': totalsport,
        'totalpolitics': totalpolitics,
        'totalbusiness': totalbusiness,
        'totalarts': totalarts
    }

    return render(request, 'home/index.html', context)


def news(request):
    is_logged_in = False
    if request.user.is_authenticated:
        is_logged_in = True
    flash_news = FlashNews.objects.all()
    news = News.objects.all().order_by("-id")
    recentpost = News.objects.all().order_by("-id")
    totalnews = News.objects.all().count()
    totalsport = News.objects.filter(category="SPORT").count()
    totalpolitics = News.objects.filter(category="POLITICS").count()
    totalbusiness = News.objects.filter(category="BUSINESS").count()
    totalarts = News.objects.filter(category="ARTS").count()

    context = {
        'is_logged_in': is_logged_in,
        'flash_news': flash_news,
        'news': news,
        'recentpost': recentpost,
        'totalnews': totalnews,
        'totalsport': totalsport,
        'totalpolitics': totalpolitics,
        'totalbusiness': totalbusiness,
        'totalarts': totalarts
    }
    return render(request, 'home/news.html', context)


def singlenews(request, slug):
    is_logged_in = False
    if request.user.is_authenticated:
        is_logged_in = True
    flash_news = FlashNews.objects.all()
    news = News.objects.all().order_by("-id")
    singlenews = News.objects.get(slug=slug)
    tags = singlenews.tags.split("|")
    recentpost = News.objects.all().order_by("-id")
    totalnews = News.objects.all().count()
    totalsport = News.objects.filter(category="SPORT").count()
    totalpolitics = News.objects.filter(category="POLITICS").count()
    totalbusiness = News.objects.filter(category="BUSINESS").count()
    totalarts = News.objects.filter(category="ARTS").count()
    context = {
        'is_logged_in': is_logged_in,
        'flash_news': flash_news,
        'news': news,
        'singlenews': singlenews,
        'tags': tags,
        'recentpost': recentpost,
        'totalnews': totalnews,
        'totalsport': totalsport,
        'totalpolitics': totalpolitics,
        'totalbusiness': totalbusiness,
        'totalarts': totalarts
    }
    return render(request, 'home/singlenews.html', context)
