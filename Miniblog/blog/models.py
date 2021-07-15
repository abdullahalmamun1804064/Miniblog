from django.db import models

# Post
class post(models.Model):
    title=models.CharField(max_length=200)
    disc=models.TextField()
    def __str__(self):
        return self.title


