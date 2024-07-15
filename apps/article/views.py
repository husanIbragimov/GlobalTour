from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView

from .models import Article


class ArticleListView(ListView):
    template_name = 'article/article.html'
    paginate_by = 1
    model = Article

    def get_queryset(self):
        query_params = self.request.GET
        print(query_params)
        return Article.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ArticleDetailView(View):
    template_name = 'article/article-detail.html'

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, slug=kwargs['slug'])
        comments = article.comments.filter(parent__isnull=True).order_by('-id')
        related_articles = Article.objects.exclude(id=article.id).order_by('-id')[:3]
        context = {
            'article': article,
            'comments': comments,
            'related_articles': related_articles
        }
        return render(request, self.template_name, context)
