from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Mobile(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=100, unique=True)  # Model name is unique
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    screen_size = models.DecimalField(max_digits=4, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('+', '+'), ('-', '-')])
    manufacturer_country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.brand.name} {self.model}"
