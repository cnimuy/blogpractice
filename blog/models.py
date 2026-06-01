from django.db import models
from accounts.models import CustomUser

class Blog(models.Model):
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField(default="default")

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, null=True, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment