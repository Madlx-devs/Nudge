from django.db import models
from django.conf import settings
# Create your models here.

class nudges (models.Model):
    content = models.TextField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE , related_name='nudges')
    created_at = models.DateTimeField(auto_now_add=True)
    images= models.ImageField(upload_to='static/media')

    

    def __str__(self):
        return self.author
