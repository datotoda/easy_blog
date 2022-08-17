from rest_framework import serializers

import blog.models
import user.models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:user-detail')
    is_active = serializers.BooleanField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)

    class Meta:
        model = user.models.User
        fields = ['url', 'username', 'email', 'first_name', 'last_name',
                  'phone_number', 'image_url', 'is_active', 'is_superuser']


class ColorSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:color-detail')

    class Meta:
        model = blog.models.Color
        fields = ['url', 'value']


class TagSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:tag-detail')
    color = serializers.HyperlinkedRelatedField(many=False, view_name='api:color-detail', read_only=True)

    class Meta:
        model = blog.models.Tag
        fields = ['url', 'value', 'color', 'updated_at', 'created_at']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:comment-detail')
    user = serializers.HyperlinkedRelatedField(many=False, view_name='api:user-detail', read_only=True)

    class Meta:
        model = blog.models.Comment
        fields = ['url', 'user', 'value', 'updated_at', 'created_at']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:post-detail')
    user = serializers.HyperlinkedRelatedField(many=False, view_name='api:user-detail', read_only=True)
    tags = serializers.HyperlinkedRelatedField(many=True, view_name='api:tag-detail', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = blog.models.Post
        fields = ['url', 'title', 'value', 'user', 'tags', 'image_url', 'slug', 'updated_at', 'created_at', 'comments']


