# In the "CommentApp" app, create a model named "Comment" with the following fields:
# Content (TextField)
# Author (CharField)
# Published Date (DateTimeField)
# Post (ForeignKey to the "Post" model)

from django.db import models
from BlogApp.models import Post

class Comment(models.Model):
    content = models.TextField()
    author  = models.CharField(max_length=200)
    published_date = models.DateTimeField(auto_now_add=True)
    post    = models.ForeignKey(Post, on_delete=models.CASCADE)
