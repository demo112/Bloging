import markdown
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import ArticlePost
from .forms import ArticlePostForm


# Create your views here.
def article_list_test(request):
    return HttpResponse("Hello World!")


def article_list(request):
    # 取出所有博客文章
    articles = ArticlePost.objects.all()
    # 需要传递给模板（templates）的对象
    # todo 消除markdown标志符以纯文本显示
    list_context = {'articles': articles}
    # render函数：载入模板，并返回context对象
    return render(request, 'article/list.html', list_context)


# def article_detail(request, article_id):
#     """普通加载版本"""
#     # todo 返回文章列表 暂时处理变量冲突
#     global context
#     while True:
#         try:
#             article = ArticlePost.objects.get(id=article_id)
#             # 需要传递给模板的对象
#             context = {'article': article}
#             # 载入模板，并返回context对象
#             break
#         except Exception as err:
#             print(err)
#             # todo 返回文章列表
#             break
#         finally:
#             return render(request, 'article/detail.html', context)


def article_detail(request, article_id):
    try:
        article = ArticlePost.objects.get(id=article_id)
        # 将markdown语法渲染成html样式
        article.body = markdown.markdown(
            article.body,
            extensions=[
                # 包含 缩写、表格等常用扩展
                'markdown.extensions.extra',
                # 语法高亮扩展
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ],
        )
        context = {'article': article}
        return render(request, 'article/detail.html', context)
    except Exception as e:
        print(e)
        # todo 返回404页面


def article_create(request):
    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            new_article = article_post_form.save(commit=False)
            # todo 后期加入选择作者
            new_article.author = User.objects.get(id=1)
            new_article.save()
            return redirect("article:article_list")
        else:
            # todo 返回404页面
            context = request.url
            return render(request, 'err/not_found_404.html', context)
    else:
        article_post_form = ArticlePostForm()
        context = {'article_post_form': article_post_form}
        return render(request, 'article/create.html', context)


def article_delete(request, article_id):
    article = ArticlePost.objects.get(id=article_id)
    # 调用.delete()方法删除文章
    article.delete()
    # 完成删除后返回文章列表
    return redirect("article:article_list")
