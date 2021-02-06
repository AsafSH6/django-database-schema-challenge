"""Department in hospital model."""
from django.db import models

from hospital import Hospital


class Department(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    class Meta:
        app_label = "covid_examinations"
