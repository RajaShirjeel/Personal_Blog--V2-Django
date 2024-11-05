from django.db import models

from users.models import CustomUser
from posts.models import Post

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=600, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"by - {self.user.username} -- On - {self.date}-- Text- {self.text}"