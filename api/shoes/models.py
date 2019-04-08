from django.db import models

# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=60)
    url = models.URLField(max_length=100)

    def __str__(self):
        return self.name


class ShoeType(models.Model):
    style = models.CharField(max_length=30)

    def __str__(self):
        return self.style


class ShoeColor(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Shoe(models.Model):
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    size = models.IntegerField(null=True)
    brand_name = models.CharField(max_length=20, null=True)
    material = models.CharField(max_length=20, null=True)
    fasten_type = models.CharField(max_length=20, null=True)
