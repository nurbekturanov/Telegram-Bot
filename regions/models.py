from django.db import models


class YearModel(models.Model):
    year = models.IntegerField(default=2023)
    image = models.ImageField(null=True, blank=True)
    mahalla = models.ForeignKey("MahallaModel", on_delete=models.CASCADE)
    tavsiya = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.year} - {self.mahalla}"


class ChoiceModel(models.Model):
    choice_name = models.CharField(max_length=60)

    def __str__(self):
        return self.choice_name


class MahallaModel(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    tuman = models.ForeignKey("TumanModel", on_delete=models.CASCADE)
    choices = models.ManyToManyField(ChoiceModel)

    def __str__(self):
        return self.name


class TumanModel(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    viloyat = models.ForeignKey("ViloyatModel", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ViloyatModel(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()

    def __str__(self):
        return self.name
