from django.db import models

class steganography(models.Model):
    # image = models.ImageField(upload_to='stegoImages/')
    # message = models.TextField()
    # password = models.CharField(max_length=128)
    # original_image = models.ImageField(upload_to='original_images/')
    image = models.ImageField(upload_to='stegoImages/')
    message = models.TextField()
    password = models.CharField(max_length=128)
    dest = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.image
