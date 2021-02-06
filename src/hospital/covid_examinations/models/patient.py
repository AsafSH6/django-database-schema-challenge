"""Patient model."""
from django.db import models

from person import Person
from department import Department


class Patient(Person):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
