from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.name


class Service(models.Model):
    image = models.ImageField(upload_to="service_images")
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title 


    
    