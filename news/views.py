from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now

from news.models import News, NewsFromAssociate, CommentsForNews, CommentsForTpNews
from news.service import start_collect_news_from_igromania, stop_collect_news_from_igromania


def news_list(request):
    queryset = News.objects.order_by("-timestamp").all()
    context = {
        'title': 'Новости',
        'queryset': queryset,
    }
    return render(request, 'news.html', context)


def my_news(request):
    if request.user.is_authenticated:
        queryset = News.objects.filter(news_author_id=request.user.id).order_by("-timestamp").all()
        context = {
            'title': 'Мои новости',
            'queryset': queryset,
        }
        return render(request, 'my_news.html', context)
    return HttpResponseRedirect('/accounts/login/')


def news_detail(request, news_id):
    instance = get_object_or_404(News, id=news_id)
    comments = CommentsForNews.objects.filter(news_id=news_id).order_by("-timestamp").all()
    context = {
        'title': instance.title,
        'instance': instance,
        'comments': comments,
    }

    if request.method == 'POST':
        if request.user.is_authenticated:
            comment_text = request.POST.get('content')
            comment_author = request.user.username
            CommentsForNews.objects.create(comment_text=comment_text, news_id=news_id, comment_author=comment_author)
        else:
            return HttpResponseRedirect('/accounts/login/')

    return render(request, 'news_detail.html', context)



def news_delete(request, news_id):
    if News.objects.filter(id=news_id).filter(news_author_id=request.user.id).exists() or request.user.is_superuser:
        News.objects.filter(id=news_id).delete()
        CommentsForNews.objects.filter(news_id=news_id).delete()
    return HttpResponseRedirect('/myNews/')


def news_update(request, news_id):
    if News.objects.filter(id=news_id).filter(news_author_id=request.user.id).exists() or request.user.is_superuser:
        instance = get_object_or_404(News, id=news_id)
        if request.method == 'POST':
            title = request.POST.get('title')
            content = request.POST.get('content')
            img_link = request.POST.get('img_link')
            news_author_id = request.user.id
            news_author = request.user.username
            News.objects.filter(id=news_id).update(title=title, content=content, news_author_id=news_author_id, news_author=news_author, img_link=img_link, updated=now())
            return HttpResponseRedirect('/myNews/')

        context = {
            'instance': instance,
        }
        return render(request, 'news_update.html', context)
    else:
        return HttpResponseRedirect('/accounts/login/')


def news_create(request):
    if request.user.is_staff:
        if request.method == 'POST':
            title = request.POST.get('title')
            content = request.POST.get('content')
            news_author_id = request.user.id
            news_author = request.user.username
            img_link = request.POST.get('img_link')
            if img_link == '':
                img_link = '/resources/static/img/news-1.jpg'
            from django.utils.timezone import now
            News.objects.create(title=title, content=content, news_author_id=news_author_id, img_link=img_link, news_author=news_author)
            return HttpResponseRedirect('/myNews/')

        context = {
            'title': 'Написать новость',
        }

        return render(request, 'news_create.html', context)
    else:
        return HttpResponseRedirect('/accounts/login/')


def third_party_news_detail(request, news_id):
    instance = get_object_or_404(NewsFromAssociate, id=news_id)
    comments = CommentsForTpNews.objects.filter(news_id=news_id).order_by("-timestamp").all()
    context = {
        'title': instance.title,
        'instance': instance,
        'comments': comments,
    }

    if request.method == 'POST':
        if request.user.is_authenticated:
            comment_text = request.POST.get('content')
            comment_author = request.user.username
            CommentsForTpNews.objects.create(comment_text=comment_text, news_id=news_id, comment_author=comment_author)
        else:
            return HttpResponseRedirect('/accounts/login/')

    return render(request, 'news_detail.html', context)


def third_party_news_update(request, news_id):
    if request.user.is_superuser:
        instance = get_object_or_404(NewsFromAssociate, id=news_id)
        if request.method == 'POST' and request.user.is_superuser:
            title = request.POST.get('title')
            content = request.POST.get('content')
            img_link = request.POST.get('img_link')
            news_author = instance.news_author
            NewsFromAssociate.objects.filter(id=news_id).update(title=title, content=content, news_author=news_author, img_link=img_link, updated=now())
            return HttpResponseRedirect('/thirdPartyNews/')

        context = {
            'instance': instance,
        }
        return render(request, 'news_update.html', context)
    else:
        return HttpResponseRedirect('/thirdPartyNews/')


def third_party_news_delete(request, news_id):
    if request.user.is_superuser:
        NewsFromAssociate.objects.filter(id=news_id).delete()
        CommentsForTpNews.objects.filter(news_id=news_id).delete()
    return HttpResponseRedirect('/thirdPartyNews/')


def third_party_news(request):
    queryset = NewsFromAssociate.objects.order_by("-timestamp").all()
    context = {
        'title': 'Новости партнёров',
        'queryset': queryset
    }
    return render(request, 'third_party_news.html', context)


def start_gen(request):
    if request.user.is_superuser:
        start_collect_news_from_igromania()
    return HttpResponseRedirect('/thirdPartyNews/')


def stop_gen(request):
    if request.user.is_superuser:
        stop_collect_news_from_igromania()
    return HttpResponseRedirect('/thirdPartyNews/')
