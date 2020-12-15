# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['name'])
        ]


class Department(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE,
                                 related_name="departments", null=False,
                                 blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1,
                              choices=[('M', 'Male'), ('F', 'Female'),
                                       ('O', 'Other')], null=False,
                              blank=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class HospitalWorker(Person):
    POSITION_DOCTOR = 'Doctor'
    POSITION_NURSE = 'Nurse'
    departments = models.ManyToManyField(Department, related_name="workers",
                                         blank=False)
    position = models.CharField(max_length=10,
                                choices=[(POSITION_DOCTOR, POSITION_DOCTOR),
                                         (POSITION_NURSE, POSITION_NURSE)],
                                null=False, blank=False)

    class Meta:
        indexes = [
            models.Index(fields=['position'])
        ]


class Patient(Person):
    pass


class ExaminationResult(models.Model):
    RESULT_HEALTHY = 'Healthy'
    RESULT_CORONA = 'Corona'
    RESULT_BOTISM = 'Botism'
    RESULT_DEAD = 'Dead'

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,
                                related_name="results", null=False, blank=False)
    time = models.DateTimeField(null=False, blank=False, auto_now_add=False,
                                auto_now=False)
    examiner = models.ForeignKey(HospitalWorker, on_delete=models.CASCADE,
                                 related_name="results", null=False,
                                 blank=False)
    result = models.CharField(max_length=1,
                              choices=[(RESULT_HEALTHY, RESULT_HEALTHY),
                                       (RESULT_CORONA, RESULT_CORONA),
                                       (RESULT_BOTISM, RESULT_BOTISM),
                                       (RESULT_DEAD, RESULT_DEAD)],
                              null=False, blank=False)

    def __str__(self):
        return "%s %s" % (
            self.patient.name, str(self.time.strftime("%d-%m-%Y %H:%M")))

    class Meta:
        indexes = [
            models.Index(fields=['result'])
        ]
