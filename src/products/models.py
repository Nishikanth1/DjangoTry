from django.db import models
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    title       = models.CharField(max_length=100)
    price       = models.DecimalField(max_digits=1000, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    summary = models.TextField(default="this is default")
    featured = models.BooleanField(default=False)# blank is for showing the user, null is for database entry()

    def get_absolute_url(self):
        #return f"/products/{self.id}"
        return reverse('products:product-detail', kwargs={"id": self.id})
