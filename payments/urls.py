from django.urls import path
from . import views

app_name = 'payments'
urlpatterns = [
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
]
