from rest_framework import viewsets, permissions

import user.models
from restapi.serializers import UserSerializer
from restapi import permisions as my_permissions


class UserViewSet(viewsets.ModelViewSet):
    queryset = user.models.User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, my_permissions.IsUserOrReadOnly]

