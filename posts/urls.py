from django.urls import path
from posts import views

urlspatterns = [
    path('posts/', views.PostList.as_view()),
]