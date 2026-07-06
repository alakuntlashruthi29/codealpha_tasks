from django.db import models

class Post(models.Model):
    username = models.CharField(max_length=100)
    content = models.TextField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.username