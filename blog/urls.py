from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('post/<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/', views.PostListlView.as_view(), name='post-list'),
    path('new_post/', views.PostCreateView.as_view(), name='post-add'),
    path('post/<slug:slug>/edit', views.PostEditView.as_view(), name='post-edit'),
    path('post/<slug:slug>/delete', views.PostDeleteView.as_view(), name='post-delete'),
]
