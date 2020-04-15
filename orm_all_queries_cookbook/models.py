from django.db import models


# Create your models here.

class Country(models.Model):
    country_name = models.CharField(max_length=100)

    class Meta:
        db_table = "countries"


class State(models.Model):
    state_name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        db_table = "states"


class City(models.Model):
    city_name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        db_table = "cities"
