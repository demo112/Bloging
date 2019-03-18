from django import forms
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField()
    # todo 密码md5加密
    password = forms.CharField()


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = {'username', 'email'}
        # fields = {'username', 'email', 'is_active', 'is_staff', 'date_joined', 'first_name', 'last_name', 'last_login'}

    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password') == data.get("password2"):
            return data.get('password')
        else:
            # todo Ajax动态加载
            raise forms.ValidationError('密码不一致请重新输入')
