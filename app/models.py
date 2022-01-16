from django.conf import settings
from django.db import models

# Create your models here.

class Shape(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    TRIANGLE = 'triangle'
    RECTANGLE = 'rectangle'
    SQUARE = 'square'
    DIAMOND = 'diamond'
    SHAPE_CHOICES = [
        (TRIANGLE, 'triangle'),
        (RECTANGLE, 'rectangle'),
        (SQUARE, 'square'),
        (DIAMOND, 'diamond'),
    ]
    type = models.CharField(max_length=20, choices= SHAPE_CHOICES)
    # type = models.CharField(max_length=20, choices= SHAPE_CHOICES, default='triangle')
    height = models.FloatField()
    width = models.FloatField()