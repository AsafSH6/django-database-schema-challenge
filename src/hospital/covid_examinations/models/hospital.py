"""Hospital model."""
from django.db import models


class Hospital(models.Model):
    city = models.CharField(max_length=30, db_index=True,
                            blank=False, null=False)
    name = models.CharField(primary_key=True, max_length=30, blank=False,
                            null=False)

    class Meta:
        app_label = "covid_examinations"
