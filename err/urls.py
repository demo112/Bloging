# 引入path
from django.urls import path
# 本地模块
from err import views

# 正在部署的应用的名称
# Django2.0之后，app的urls.py必须配置app_name，否则会报错

app_name = 'err'

urlpatterns = [
    # 目前还没有urls
    path('not_found_404/', views.err_404, name='err_404'),
    path('wrong_method/', views.err_method, name='err_method'),
    path('no_right/', views.err_no_right, name='err_no_right'),

]
