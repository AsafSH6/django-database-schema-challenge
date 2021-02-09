"""Department in hospital model."""
from django.db import models

from hospital import Hospital


class Department(models.Model):
    name = models.CharField(primary_key=True, max_length=30, blank=False,
                            null=False)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE,
                                 related_name="departments", blank=False,
                                 null=False)

    class Meta:
        app_label = "covid_examinations"
