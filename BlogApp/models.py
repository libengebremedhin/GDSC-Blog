# In the "BlogApp" app, extend the "Post" model with the following fields and constraints:
# Title (CharField, unique=True)
# Content (TextField)
# Category (CharField)
# Image (ImageField)
# Tags (ArrayField(CharField))

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
    # You guys mentioned that this tags model should be an ArrayField, but when I used it, it was saying it only works on a PostgreSQL database. So, I created another model called 'tags' and included it.
    def __str__(self):
        return self.title