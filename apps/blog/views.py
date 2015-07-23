#!/usr/bin/python
# -*- coding: UTF-8 -*-

from .models import Article
from .models import Category, Tag
from collections import defaultdict
from collections import OrderedDict
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, render_to_response, get_object_or_404

def PaginateArticles(articles, per_page, page_num):
    paginator = Paginator(articles, per_page)
    try:
        articles = paginator.page(page_num)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return articles

def Home(req):
    articles = Article.objects.order_by('-create_date')
    articles = PaginateArticles(articles, 6, req.GET.get('page'))
    context = {'articles':articles, 'column':'home'}
    return render_to_response('home.html', context)
        
def Archives(req):
    articles = Article.objects.order_by('-create_date')
    years = list()
    articles_by_year = defaultdict(list)
    year = articles[0].create_date.year
    years.append(year)
    for article in articles:
        cur_year = article.create_date.year
        articles_by_year[cur_year].append(article)
        if year != cur_year:
            year = cur_year
            years.append(year)

    archives = OrderedDict()
    for year in years:
        archives[year] = articles_by_year[year]
        
    context = {'archives':archives, 'column':'archives'}
    return render_to_response('archives.html', context)

def ArticlesOfTag(req, slug):
    cur_tag = get_object_or_404(Tag, slug=slug)
    articles = Article.objects.filter(tag=cur_tag).order_by('-create_date')
    articles = PaginateArticles(articles, 6, req.GET.get('page'))
    context = {'articles':articles, 'column':'tag'}
    return render_to_response('articles_of_tag.html', context)

def ArticlesOfCategory(req, slug):
    cur_category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(category
        =cur_category).order_by('-create_date')
    articles = PaginateArticles(articles, 6, req.GET.get('page'))
    context = {'articles':articles, 'column':'category'}
    return render_to_response('articles_of_category.html', context)

class ArticleDetail(DetailView):
    model = Article
    template_name = 'article_detail.html'
