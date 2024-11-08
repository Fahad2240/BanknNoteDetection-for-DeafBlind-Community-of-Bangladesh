from django.db import models

# Create your models here.
class realtimeimg(models.Model):
    image=models.ImageField(upload_to='Detect_images',blank=True,null=True)