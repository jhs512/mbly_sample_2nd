from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('join/', views.join, name='join'),
    path('logout/', views.logout, name='logout'),
    path('find_username/', views.find_username, name='find_username'),
    path('signin/kakao/', views.kakao_login, name="kakao_signin"),
    path('signin/kakao/callback/', views.kakao_login_callback, name="kakao_signin_callback"),
]
