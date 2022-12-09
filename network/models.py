from django.contrib.auth.models import AbstractUser, User
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    content = models.CharField(max_length=160)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    date  = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(User, default=None, blank=True)
    def __str__(self):
        return f"Post {self.id} made by {self.user} on {self.date.strftime('%d %b %Y %H:%M:%S')}"

    @property
    def num_likes(self):
        return self.liked.all().count()

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike','Unlike'),
)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.post)

class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_following")
    user_follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_followed")

    def __str__(self):
        return f"{self.user} is following {self.user_follower}"

    