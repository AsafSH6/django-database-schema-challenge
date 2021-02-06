"""Person model."""
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Person(models.Model):
    GENDERS = tuple({
        "M": "Male",
        "H": "Habra",
        "O": "Other",
        "F": "Female",
    }.items())

    name = models.CharField(max_length=30)
    gender = models.CharField(choices=GENDERS, max_length=20)
    age = models.IntegerField(validators=[MaxValueValidator(120),
                                          MinValueValidator(18)])

    class Meta:
        abstract = True
        app_label = "covid_examinations"
