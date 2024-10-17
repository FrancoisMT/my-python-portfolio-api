from django.db import models

class Message(models.Model):
    title = models.CharField(max_length=255)  
    content = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True) 

    