"""Hospital model."""
from django.db import models


class Hospital(models.Model):
    city = models.CharField(max_length=30)
    name = models.CharField(primary_key=True, max_length=30)

    class Meta:
        app_label = "covid_examinations"
