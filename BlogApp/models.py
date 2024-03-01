from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='blog/')
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.title
