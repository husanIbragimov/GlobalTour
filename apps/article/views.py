from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import View

from .models import Article


class ArticleListView(View):
    template_name = 'article/article.html'
    paginate_by = 9
    model = Article

    def get(self, request, *args, **kwargs):
        query_params = self.request.GET
        page = query_params.get('page')
        search = query_params.get('search')
        if search:
            articles = get_list_or_404(Article.objects.filter(Q(name__icontains=search) | Q(content__icontains=search)).order_by('-id'))
        else:
            articles = get_list_or_404(Article.objects.all().order_by('-id'))

        paginator = Paginator(articles, self.paginate_by)
        object_list = paginator.get_page(page)
        return render(request, self.template_name, {'object_list': object_list})


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

    def post(self, request, *args, **kwargs):
        url = request.META.get('HTTP_REFERER')
        article = get_object_or_404(Article, slug=kwargs['slug'])
        article.comments.create(
            name=request.POST.get('name'),
            phone_number=request.POST.get('phone_number'),
            content=request.POST.get('message'),
            is_published=False
        )
        message = 'Sizning sharhingiz qabul qilindi. Tez orada siz bilan bog\'lanamiz.'
        messages.success(request, message, extra_tags='success')
        return redirect(url)
