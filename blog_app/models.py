from django.db import models

# Create your models here.

class Blogpost(models.Model):
    author = models.CharField(max_length = 12)
    image = models.ImageField(upload_to='uploads/')
    post = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.author 