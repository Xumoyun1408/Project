from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Air(models.Model):
    name = models.CharField(max_length=100)
    aholi = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='airs')
    image = models.ImageField(upload_to='air_images', null=True)

    def __str__(self):
        return f"{self.name}"

class Reys(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class City(models.Model):
    name = models.CharField(max_length=100)
    aholi = models.PositiveIntegerField()
    reys = models.ForeignKey(Reys, on_delete=models.CASCADE, related_name='reys')
    image = models.ImageField(upload_to='reys_images', null=True)

    def __str__(self):
        return f"{self.name}"