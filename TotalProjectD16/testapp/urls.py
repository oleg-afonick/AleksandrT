from django.urls import path

from .views import ArticleList, ArticleCreate, ArticleDetail, ArticleUpdate, ArticleDelete, IndexView, CommentCreate

urlpatterns = [
    path('', ArticleList.as_view(), name='article_list'),
    path('create/', ArticleCreate.as_view(), name='article_create'),
    path('<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
    path('<int:pk>/update/', ArticleUpdate.as_view(), name='article_update'),
    path('<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
    path('<int:pk>/comments/', IndexView.as_view(), name='comment'),
    path('<int:pk>/comment/create/', CommentCreate.as_view(), name='comment_create'),
]
