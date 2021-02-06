"""Hospital worker model."""
from django.db import models

from person import Person
from department import Department


class Worker(Person):
    JOBS = tuple({
        "D": "Doctor",
        "N": "Nurse",
    }.items())

    job = models.CharField(choices=JOBS, max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        app_label = "covid_examinations"
