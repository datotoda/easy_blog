from django.contrib.auth.decorators import login_required as lr
from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('post/<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/', views.PostListlView.as_view(), name='post-list'),
    path('my_posts/', views.MyPostListlView.as_view(), name='my-post-list'),
    path('new_post/', lr(views.PostCreateView.as_view()), name='post-add'),
    path('post/<slug:slug>/edit', lr(views.PostEditView.as_view()), name='post-edit'),
    path('post/<slug:slug>/delete', lr(views.PostDeleteView.as_view()), name='post-delete'),
]
