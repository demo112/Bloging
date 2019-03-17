from django import forms
from .models import ArticlePost


class ArticlePostForm(forms.ModelForm):
    """写文章的表单类"""
    class Meta:
        # 指明数据模型来源

        model = ArticlePost
        # todo 是否可以多添加几个字段
        # 定义表单包含的字段
        fields = ('title', 'body')