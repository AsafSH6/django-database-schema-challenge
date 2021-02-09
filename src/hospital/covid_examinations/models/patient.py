"""Patient model."""
from django.db import models

from person import Person
from department import Department


class Patient(Person):
    personal_information = models.ForeignKey(Person, blank=False, null=False,
                                             on_delete=models.CASCADE,
                                             related_name=
                                             "treating_departments")
    department = models.ForeignKey(Department, on_delete=models.CASCADE,
                                   related_name="patients", blank=False,
                                   null=False)
