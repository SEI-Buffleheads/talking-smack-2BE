from rest_framework import serializers

from.models import Post, Comment,User

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model=Post
    fields='__all__'

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model=Comment
    field='__all__'

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model=User
    field='__all__'

