from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_tweet, name='create_tweet'),
    path('success/', views.success, name='tweet_success'),
]