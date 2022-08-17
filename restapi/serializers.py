from rest_framework import serializers

import user.models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:user-detail')
    is_active = serializers.BooleanField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)

    class Meta:
        model = user.models.User
        fields = ['url', 'username', 'email', 'first_name', 'last_name',
                  'phone_number', 'image_url', 'is_active', 'is_superuser']
