from rest_framework import viewsets, permissions

import blog.models
import user.models
from restapi import serializers
from restapi import permisions as my_permissions


class MultipleSerializerMixin:
    serializers = None

    def get_serializer_class(self):
        if self.serializers:
            return self.serializers.get(self.action, self.serializers.get('default', super().get_serializer_class()))
        return super().get_serializer_class()


class UserViewSet(MultipleSerializerMixin, viewsets.ModelViewSet):
    queryset = user.models.User.objects.all()
    serializer_class = serializers.UserSerializer
    serializers = {
        'create': serializers.UserCreateSerializer,
    }
    permission_classes = [permissions.IsAuthenticated, my_permissions.IsUserOrReadOnly]


class ColorViewSet(viewsets.ModelViewSet):
    queryset = blog.models.Color.objects.all()
    serializer_class = serializers.ColorSerializer
    permission_classes = [my_permissions.IsSuperUserOrReadOnly]


class TagViewSet(viewsets.ModelViewSet):
    queryset = blog.models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
    permission_classes = [my_permissions.IsSuperUserOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = blog.models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [my_permissions.IsOwnerOrReadOnly]


class PostViewSet(viewsets.ModelViewSet):
    queryset = blog.models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [my_permissions.IsOwnerOrReadOnly]
