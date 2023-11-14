from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Предыдущий url входа
    # path('login/', views.user_login, name='login'),
    # url-адреса для входа и выхода
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    
    # url адреса для смены пароля
    path('password-change/', 
        auth_views.PasswordChangeView.as_view(), 
        name='password-change'),
    path('password-change/done/', 
        auth_views.PasswordChangeDoneView.as_view(), 
        name='password-change_done'),
    path('', views.dashboard, name='dashboard'),
    
]
