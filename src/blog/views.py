from django.shortcuts import render, get_object_or_404
from django.urls import reverse

# Create your views here.
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, ListView, DeleteView)

from .models import Articles
from .forms import ArticleModelForm


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'  # default template is <app_name>/<modelname>_list.html
    queryset = Articles.objects.all()

class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Articles.objects.all()
    #success_url = "somepath"
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(ArticleCreateView, self).form_valid(form)

    #def get_success_url(self):
    #    return 'somepath'

class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Articles.objects.all()
    #success_url = "somepath"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Articles, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(ArticleUpdateView, self).form_valid(form)

class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    #queryset = Articles.objects.all() # considers whole DB if not filtered
    #queryset = Articles.objects.filter(id__gt=1)
    #success_url = /blog/

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Articles, id=id_)

    def get_success_url(self):
        return reverse('articles:article-list')
class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    #queryset = Articles.objects.all() # considers whole DB if not filtered
    #queryset = Articles.objects.filter(id__gt=1)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Articles, id=id_)
