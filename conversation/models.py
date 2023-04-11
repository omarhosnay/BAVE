from django.db import models
from django.contrib.auth.models  import User
# Create your models here.
from item.models import Item

class Conv(models.Model):
    item = models.ForeignKey(Item, related_name='conversation', on_delete=models.CASCADE)
    members =  models.ManyToManyField(User ,   related_name='conversation' , )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-modified_at',)
        
        
class ConvMessage(models.Model):
    conv = models.ForeignKey(Conv, related_name='message' , on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)
    class Meta:
        ordering = ('-created_at',)