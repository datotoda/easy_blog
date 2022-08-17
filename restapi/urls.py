from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restapi import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'colors', views.ColorViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'posts', views.PostViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]
