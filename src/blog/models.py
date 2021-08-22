from django.db import models
from django.urls.base import reverse
# Create your models here.

class Articles(models.Model):
    title   = models.CharField(max_length=120)
    content = models.TextField()
    active = models.BooleanField()

    def get_absolute_url(self):
        #return f"/products/{self.id}"
        return reverse('articles:article-detail', kwargs={"id": self.id})