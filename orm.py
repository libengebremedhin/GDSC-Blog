import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GDSCBlog.settings')
import django
django.setup()

from BlogApp.models import Post, Tag
from CommentApp.models import Comment

tag1 = Tag.objects.create(name="django")
tag2 = Tag.objects.create(name="blog")
tag3 = Tag.objects.create(name="aastu")

one = Post.objects.create(title="Ludis", content="Creating content for Ludis", category="Tech")
two = Post.objects.create(title="Leul", content="Content for the second post", category="Science")
three = Post.objects.create(title="Leulseged", content="Content for the third post", category="Travel")

one.tags.set([tag1, tag2])
two.tags.set([tag3, tag2])
three.tags.set([tag1, tag3])

tech_posts = Post.objects.filter(category="Tech")
print("Posts in Tech category:", tech_posts)


one.content = "This is the updated content for Ludis"
one.save()

three.delete()

comment1 = Comment.objects.create(content="Comment for the first post", author="User1", post=one)
comment2 = Comment.objects.create(content="Comment for the second post", author="User2", post=two)
comment3 = Comment.objects.create(content="Comment for the third post", author="User3", post=three)

one_comments = Comment.objects.filter(post=one)
print("Comments for the first post:", one_comments)

comment1.content = "Updated comment for the first post"
comment1.save()

comment3.delete()
