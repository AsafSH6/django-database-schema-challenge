"""Department in hospital model."""
from django.db import models

from hospital import Hospital


class Department(models.Model):
    name = models.CharField(null=False,
                            blank=False,
                            max_length=30,
                            primary_key=True)

    hospital = models.ForeignKey(Hospital,
                                 null=False,
                                 blank=False,
                                 on_delete=models.CASCADE,
                                 related_name="departments")

    class Meta:
        app_label = "covid_examinations"
