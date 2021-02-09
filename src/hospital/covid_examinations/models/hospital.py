"""Hospital model."""
from django.db import models


class Hospital(models.Model):
    city = models.CharField(null=False,
                            blank=False,
                            max_length=30,
                            db_index=True)

    name = models.CharField(null=False,
                            blank=False,
                            max_length=30,
                            primary_key=True)

    class Meta:
        app_label = "covid_examinations"
