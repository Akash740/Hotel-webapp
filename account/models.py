from django.db import models

class hotel(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
    image=models.ImageField(upload_to='account/images',default="")