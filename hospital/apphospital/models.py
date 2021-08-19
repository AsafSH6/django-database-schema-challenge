# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models


class Hospital(models.Model):
    name = models.CharField(db_index=True, max_length=200, default='', null=False, blank=False)
    city = models.CharField(max_length=200, default='', null=False, blank=False)

    def __str__(self):
        return "ID{} - {}".format(self.pk, self.name)


class Department(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE,
                                 related_name='departments',
                                 default='',
                                 null=False,
                                 blank=False)
    name = models.CharField(db_index=True, max_length=200, default='', null=False, blank=False)

    def __str__(self):
        return "department {}".format(self.name)


class People(models.Model):
    GENDER_TYPES = [('Male', 'Male'),
                    ('Female', 'Female'),
                    ('Other', 'Other')]
    name = models.CharField(db_index=True, max_length=200, default='', null=False, blank=False)
    age = models.CharField(max_length=200, default=0, null=False, blank=True)
    gender = models.CharField(max_length=200, choices=GENDER_TYPES, default="Male", null=False, blank=False)

    def __str__(self):
        return self.name


class Worker(People):
    JOBS = [('Doctor', 'Doctor'),
            ('Nurse', 'Nurse')]
    role = models.CharField(max_length=50, choices=JOBS, default='Doctor', null=False, blank=False)
    department = models.ManyToManyField(Department, null=False, blank=False)

    def __str__(self):
        return "{} {} works in {}".format(self.role, self.name, self.department)


class Patient(People):
    department_in = models.ForeignKey(Department, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return "{} in {}".format(self.people_name, self.department_in)


class MedicalExamination(models.Model):
    HEALTY = 'Healty'
    CORONA = 'Corona'
    BOTISM = 'Botism'
    DEAD = 'Dead'
    RESULTS = [(HEALTY, HEALTY),
               (CORONA, CORONA),
               (BOTISM, BOTISM),
               (DEAD, DEAD)]
    date = models.DateTimeField("exam date", auto_now=False, auto_now_add=False
                                )
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, null=False, blank=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=False, blank=False)
    result = models.CharField(max_length=20, choices=RESULTS, default=HEALTY, null=False, blank=False)

    def __str__(self):
        return "date: {} exam result {}".format(self.date,
                                                self.result)
