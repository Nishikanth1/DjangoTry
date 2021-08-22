from django.shortcuts import render

# Create your views here.
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, ListView, DeleteView)

from .models import Articles


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'  # default template is <app_name>/<modelname>_list.html
    queryset = Articles.objects.all()

class ArticleDetailView(DetailView):
    #template_name = 'articles/article_detail.html'
    queryset = Articles.objects.all()
