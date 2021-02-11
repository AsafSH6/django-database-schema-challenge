"""Hospital worker model."""
from django.db import models

from person import Person
from department import Department


class HospitalWorker(models.Model):
    NURSE = "Nurse"
    DOCTOR = "Doctor"

    JOBS = tuple(
        {
            NURSE: NURSE,
            DOCTOR: DOCTOR,
        }.items()
    )

    job = models.CharField(null=False,
                           blank=False,
                           choices=JOBS,
                           max_length=20)

    department = models.ForeignKey(Department,
                                   null=False,
                                   blank=False,
                                   related_name="workers",
                                   on_delete=models.CASCADE)

    personal_information = models.ForeignKey(Person,
                                             null=False,
                                             blank=False,
                                             primary_key=True,
                                             on_delete=models.CASCADE,
                                             related_name=
                                             "hospital_position")

    class Meta:
        app_label = "covid_examinations"
