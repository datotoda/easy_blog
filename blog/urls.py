from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('post/<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/', views.PostListlView.as_view(), name='post-list'),
]
