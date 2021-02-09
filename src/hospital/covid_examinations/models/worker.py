"""Hospital worker model."""
from django.db import models

from person import Person
from department import Department


class HospitalWorker(Person):
    NURSE = "Nurse"
    DOCTOR = "Doctor"

    JOBS = tuple(
        {
            NURSE: NURSE,
            DOCTOR: DOCTOR,
        }.items()
    )

    personal_information = models.OneToOneField(Person, blank=False,
                                                null=False,
                                                primary_key=True,
                                                on_delete=models.CASCADE,
                                                related_name=
                                                "hospital_position")
    job = models.CharField(choices=JOBS, max_length=20, blank=False,
                           null=False)
    department = models.ForeignKey(Department, related_name="workers",
                                   on_delete=models.CASCADE, blank=False,
                                   null=False)

    class Meta:
        app_label = "covid_examinations"
