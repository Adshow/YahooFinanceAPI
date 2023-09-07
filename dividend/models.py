from django.db import models

# Create your models here.
class Dividend(models.Model):
    symbol = models.CharField(max_length=10)
    year = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.symbol} - {self.year}"