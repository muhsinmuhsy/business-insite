from django.db import models

# Create your models here.


class Service(models.Model):
    image = models.ImageField(upload_to='service_images/', null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) :
        return self.title