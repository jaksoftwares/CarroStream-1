from django.urls import path
from . import views

urlpatterns = [
    # Define your routes here, e.g.,
path('blog', views.blog, name='blog'),
path ('newsletter', views.news_letter, name = 'newsletter' ),

]
