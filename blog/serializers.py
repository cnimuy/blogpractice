from rest_framework import serializers
from accounts.serializers import CustomUserSerializer
from blog.models import Blog, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'blog', 'comment', 'created_at']
        read_only_fields = ['blog']

class BlogListSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = ["id", "title", "body", "user", "created_at"]


class BlogDetailSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ["id", "title", "body", "user", "created_at", "comments"]