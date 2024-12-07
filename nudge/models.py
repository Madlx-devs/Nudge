from django.db import models
from django.conf import settings
# Create your models here.

class nudge (models.Model):
    content = models.TextField(max_length=300)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE , related_name='nudges')
    created_at = models.DateTimeField(auto_now_add=True )
    images= models.ImageField(upload_to='media' , blank=True , null=True)

    

    def __str__(self):
        return self.content
