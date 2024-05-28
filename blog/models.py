from django.db import models
from utils.models import BaseModel
from taggit.managers import TaggableManager
from django.utils.text import slugify
from users.models import User



class Category(BaseModel):
    title = models.CharField(max_length=31)
    slug = models.SlugField(max_length=255, blank=True, null=True,
                            unique_for_date='created_at')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Post(BaseModel):

    title = models.CharField(max_length=31)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    is_recommended = models.BooleanField(default=False)

    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='author_posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='posts')
    is_active = models.BooleanField(default=False)

    tags = TaggableManager()
    views = models.IntegerField(default=0, editable=False)
    slug = models.SlugField(max_length=255, blank=True, null=True,
                            unique_for_date='created_at')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at'])
        ]


class Comment(BaseModel):
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.comment


