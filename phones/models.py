from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(null=False)
    image = models.ImageField()
    price = models.FloatField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()
