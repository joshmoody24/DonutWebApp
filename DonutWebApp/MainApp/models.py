from django.db import models

class DonutType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Donut(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey('DonutType', on_delete=models.CASCADE)
    description = models.TextField()
    price = models.IntegerField()
    image = models.URLField()
    
    @property
    def formattedPrice(self):
        return f'${self.price/100}'

    def __str__(self):
        return self.name
