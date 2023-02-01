from django.db import models

class products(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products_images', null=True, blank=True)

    def __str__(self):
        return self.name

class category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, default= 'Descripción')

    def __str__(self):
        return self.name

class providers(models.Model):
    name = models.CharField(max_length=50)
    provides = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name
