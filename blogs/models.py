import uuid
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Blogs(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date',]     #ordering our blogs to show the new new blogs first
    
    def get_absolute_url(self):
        return reverse('blogs_detail', args=[str(self.id)])

# comment model created with the help of : https://tutorial-extensions.djangogirls.org/en/homework_create_more_modelshttps://tutorial-extensions.djangogirls.org/en/homework_create_more_models
class Comment(models.Model):
    blogs = models.ForeignKey(
        Blogs,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    text = models.CharField(max_length=140)
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)


    def approve(self):
        self.approved_comment = True
        self.save()
    
    class Meta:
        ordering = ['-created_date',]  #ordering our comments to show the new comments first


    def __str__(self):
        return self.text

