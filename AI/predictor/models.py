from django.db import models

# Create your models here.
class Data(models.Model):
    number_of_people = models.IntegerField(default=None)
    bedrooms = models.IntegerField(default=None)
    bathrooms = models.IntegerField(default=None)
    beds = models.IntegerField(default=None)
    minimum_nights = models.IntegerField(default=None)
    maximum_nights = models.IntegerField(default=None)
    number_of_reviews = models.IntegerField(default=None)
