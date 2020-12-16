# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False,
                            db_index=True)
    city = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Department(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE,
                                 related_name="departments", null=False,
                                 blank=False)
    name = models.CharField(max_length=100, null=False, blank=False,
                            db_index=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    GENDER_MALE = "Male"
    GENDER_FEMALE = "Female"
    GENDER_OTHER = "Other"

    name = models.CharField(max_length=100, null=False, blank=False,
                            db_index=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10,
                              choices=[(GENDER_MALE, GENDER_MALE),
                                       (GENDER_FEMALE, GENDER_FEMALE),
                                       (GENDER_OTHER, GENDER_OTHER)],
                              null=False,
                              blank=False)

    def __str__(self):
        return self.name


class HospitalWorker(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=False,
                               blank=False)
    departments = models.ManyToManyField(Department, related_name="workers",
                                         blank=False, through='DepartmentWork')


class DepartmentWork(models.Model):
    POSITION_DOCTOR = 'Doctor'
    POSITION_NURSE = 'Nurse'

    hospital_worker = models.ForeignKey(HospitalWorker,
                                        on_delete=models.CASCADE, null=False,
                                        blank=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,
                                   null=False,
                                   blank=False)
    position = models.CharField(max_length=10,
                                choices=[(POSITION_DOCTOR, POSITION_DOCTOR),
                                         (POSITION_NURSE, POSITION_NURSE)],
                                null=False, blank=False)


class Patient(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=False,
                               blank=False)


class ExaminationResult(models.Model):
    RESULT_HEALTHY = 'Healthy'
    RESULT_CORONA = 'Corona'
    RESULT_BOTISM = 'Botism'
    RESULT_DEAD = 'Dead'

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,
                                related_name="examination_results", null=False,
                                blank=False)
    time = models.DateTimeField(null=False, blank=False, auto_now_add=False,
                                auto_now=False)
    examiner = models.ForeignKey(HospitalWorker, on_delete=models.CASCADE,
                                 related_name="examination_results", null=False,
                                 blank=False)
    result = models.CharField(max_length=10,
                              choices=[(RESULT_HEALTHY, RESULT_HEALTHY),
                                       (RESULT_CORONA, RESULT_CORONA),
                                       (RESULT_BOTISM, RESULT_BOTISM),
                                       (RESULT_DEAD, RESULT_DEAD)],
                              null=False, blank=False)

    def __str__(self):
        return "%s %s" % (
            self.patient.name, str(self.time.strftime("%d-%m-%Y %H:%M")))
