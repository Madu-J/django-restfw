from django.urls import path
from post import views

urlspatterns = [
    path('post/', views.PostList.as_view()),
]