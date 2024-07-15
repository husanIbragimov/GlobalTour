from django.urls import path

from .views import ArticleListView, ArticleDetailView

app_name = 'article'

urlpatterns = [
    path('list', ArticleListView.as_view(), name='article_list'),
    path('detail/<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),
]
