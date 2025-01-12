
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('password_reset', views.password_reset, name='password_reset'),
    path('password_reset_done/', views.password_reset_done, name='password_reset_done'),
    path('activate/<uidb64>/<token>/', views.activate_account, name='activate_account'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
