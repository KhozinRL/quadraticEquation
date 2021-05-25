from django.db import models

# Create your models here.


class Equation(models.Model):
    a = models.FloatField()
    b = models.FloatField()
    c = models.FloatField()
    x1 = models.FloatField()
    x2 = models.FloatField()

    x1.null = True
    x2.null = True
