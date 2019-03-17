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
        return redirect("err:err_404")


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
            return redirect("err:err_404")
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


def article_update(request, article_id):
    """
    更新文章的视图函数
    通过POST方法提交表单，更新title、body字段
    GET方法进入初始表单页面
    id： 文章的 id
    """
    article = ArticlePost.objects.get(id=article_id)
    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            return redirect('article:article_detail', article_id=article_id)
        else:
            # todo 提示后跳转新页面
            return HttpResponse("表单内容有误，请重新填写")
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 赋值上下文，将 article 文章对象也传递进去，以便提取旧的内容
        context = {'article': article, 'article_post_form': article_post_form}
        # 将响应返回到模板中
        return render(request, 'article/update.html', context)
