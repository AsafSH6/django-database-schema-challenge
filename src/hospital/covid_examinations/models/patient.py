"""Patient model."""
from django.db import models

from person import Person
from department import Department


class Patient(models.Model):
    department = models.ForeignKey(Department,
                                   null=False,
                                   blank=False,
                                   related_name="patients",
                                   on_delete=models.CASCADE)

    personal_information = models.ForeignKey(Person,
                                             null=False,
                                             blank=False,
                                             related_name="patient",
                                             on_delete=models.CASCADE)
