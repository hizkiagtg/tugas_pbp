from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class MyWatchList(models.Model):
    title = models.CharField(max_length=255)
    watched = models.BooleanField() 
    rating = models.IntegerField(validators= 
                    [MaxValueValidator(5), MinValueValidator(1)])
    release_date = models.DateField()
    review = models.TextField()
