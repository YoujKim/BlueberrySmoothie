from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('mypage/', views.InfoList.as_view(), name='mypage'),
    path('mypage/study/', views.StudyList.as_view(), name='study'),
    path('mypage/store/', views.StoreList.as_view(), name='store'),
    path('mypage/update/', views.update, name='update'),
]