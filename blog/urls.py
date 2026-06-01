from django.urls import path
from .views import BlogListAPIView, BlogDetailAPIView, CommentAPIView

app_name = 'blog'

urlpatterns = [
    path("", BlogListAPIView.as_view(), name="blog_list"),
    path("<int:blog_id>/", BlogDetailAPIView.as_view(), name="blog_detail"),
    path("<int:blog_id>/comments/", CommentAPIView.as_view(), name="comment_list"),
]