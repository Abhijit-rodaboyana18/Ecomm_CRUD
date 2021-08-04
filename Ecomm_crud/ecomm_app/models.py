from django.db import models

# Create your models here.
class ecomm_model(models.Model):
    name = models.CharField(max_length = 20)
    phone = models.IntegerField()
    email = models.EmailField(max_length = 20)
    product = models.CharField(max_length = 20)
    quantity = models.IntegerField()

