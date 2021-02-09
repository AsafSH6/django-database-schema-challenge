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

    age = models.PositiveSmallIntegerField(blank=False, null=False)
    name = models.CharField(max_length=30, db_index=True, blank=False,
                            null=False)
    gender = models.CharField(choices=GENDERS, max_length=20, blank=False,
                              null=False)

    class Meta:
        app_label = "covid_examinations"
