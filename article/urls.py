# 引入path
from django.urls import path
# 本地模块
from article import views

# 正在部署的应用的名称
# Django2.0之后，app的urls.py必须配置app_name，否则会报错

app_name = 'article'

urlpatterns = [
    # 目前还没有urls
    # path函数将url映射到视图
    path('article-list/', views.article_list, name='article_list'),
    path('article-detail/<int:article_id>/', views.article_detail, name='article_detail'),
    path('article-create/', views.article_create, name='article_create'),
    path('article-delete/<int:article_id>/', views.article_delete, name='article_delete'),
    path('article-update/<int:article_id>/', views.article_update, name='article_update'),
]
