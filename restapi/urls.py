from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restapi import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]
