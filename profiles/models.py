from django.db import models
# we have to listen to events like when a user profile is created and run some code
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from category.models import Category

# Create your models here.
# define the model of the user

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_lkftsm'
    )

    class Meta:
        ordering = ['-created_at']

    
    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)