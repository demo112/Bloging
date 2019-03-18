from django.conf.urls import url
from django.urls import path
from userprofile import views

app_name = 'userprofile'

urlpatterns = [
    path('login/', views.user_login, name='userprofile_login'),
    path('logout/', views.user_logout, name='userprofile_logout'),
    path('register/', views.user_register, name='userprofile_register'),
    path('delete/<int:id>/', views.user_delete, name='userprofile_delete')
]

urlpatterns += [
    url(r'^$', views.user_login, name='userprofile_first_open'),
]
