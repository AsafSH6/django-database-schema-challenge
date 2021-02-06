"""Corona examination model."""
from django.db import models

from worker import Worker
from patient import Patient


class Examination(models.Model):
    RESULTS = tuple({
        "H": "Healthy",
        "C": "Corona",
    }.items())

    worker = models.ForeignKey(Worker)
    patient = models.ForeignKey(Patient)
    results = models.CharField(choices=RESULTS, max_length=20)

    class Meta:
        app_label = "covid_examinations"
