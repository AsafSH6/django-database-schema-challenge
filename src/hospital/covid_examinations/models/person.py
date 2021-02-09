"""Person model."""
from django.db import models


class Person(models.Model):
    MALE = "Male"
    OTHER = "Other"
    FEMALE = "Female"

    GENDERS = tuple(
        {
            MALE: MALE,
            OTHER: OTHER,
            FEMALE: FEMALE
        }.items()
    )

    age = models.PositiveSmallIntegerField(null=False,
                                           blank=False)

    name = models.CharField(null=False,
                            blank=False,
                            max_length=30,
                            db_index=True)

    gender = models.CharField(null=False,
                              blank=False,
                              max_length=20,
                              choices=GENDERS)

    class Meta:
        app_label = "covid_examinations"
