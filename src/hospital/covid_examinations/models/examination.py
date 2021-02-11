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

    results = models.CharField(null=False,
                               blank=False,
                               choices=RESULTS,
                               max_length=20)

    time = models.DateTimeField(null=False,
                                blank=True,
                                auto_now=False,
                                auto_now_add=True)

    patient = models.ForeignKey(Patient,
                                null=False,
                                blank=False,
                                related_name="examinations_history")

    worker = models.ForeignKey(HospitalWorker,
                               null=False,
                               blank=False,
                               related_name="performed_examinations")

    class Meta:
        app_label = "covid_examinations"
