from django.db import models
from django.contrib.auth.models import User
from category.models import Category


# Create your models here.

class Post(models.Model):
    """
    Post model, related to owner, i.e. a User instance
    Default image set so that we can always reference image.url
    """
    image_filter_choices = [
    ('_1977', '1977'), ('brannan', 'Brannan'),
    ('earlybird', 'Earlybird'), ('hudson', 'Hudson'),
    ('inkwell', 'Inkwell'), ('lofi', 'Lo-Fi'),
    ('kelvin', 'Kelvin'), ('normal', 'Normal'),
    ('nashville', 'Nashville'), ('rise', 'Rise'),
    ('toaster', 'Toaster'), ('valencia', 'Valencia'),
    ('walden', 'Walden'), ('xpro2', 'X-pro II')
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='Segment')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_lkftsm', blank=True
    )

    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )

    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} | {self.title} | {self.owner}'
