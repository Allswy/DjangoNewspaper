from django.urls import path

from articles.views import ArticleListView, ArticleDetailView, ArticleNewView, ArticleUpdateView, ArticleDeleteView

app_name = 'articles'

urlpatterns = [
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', ArticleNewView.as_view(), name='article_new'),

]