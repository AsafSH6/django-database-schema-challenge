"""Corona examination model."""
from django.db import models

from patient import Patient
from worker import HospitalWorker


class Examination(models.Model):
    DEAD = "Dead"
    CORONA = "Corona"
    BOTISM = "Botism"
    HEALTHY = "Healthy"

    RESULTS = tuple(
        {
            DEAD: DEAD,
            CORONA: CORONA,
            BOTISM: BOTISM,
            HEALTHY: HEALTHY,
        }.items()
    )

    time = models.DateTimeField(auto_now=True, blank=False, null=False)
    worker = models.ForeignKey(HospitalWorker,
                               related_name="performed_examinations",
                               blank=False, null=False)
    patient = models.ForeignKey(Patient, related_name="examinations_history",
                                blank=False, null=False)
    results = models.CharField(choices=RESULTS, max_length=20, blank=False,
                               null=False)

    class Meta:
        app_label = "covid_examinations"
