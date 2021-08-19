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
    hospital = models.ForeignKey(to=Hospital, on_delete=models.CASCADE,
                                 related_name='departments',
                                 default='',
                                 null=False,
                                 blank=False)
    name = models.CharField(db_index=True, max_length=200, default='', null=False, blank=False)

    def __str__(self):
        return "{}".format(self.name)


class Person(models.Model):
    name = models.CharField(db_index=True, max_length=200, default='', null=False, blank=False)
    age = models.PositiveIntegerField(default=0, null=False, blank=True)
    gender = models.CharField(max_length=200, choices=[('Male', 'Male'),
                                                       ('Female', 'Female'),
                                                       ('Other', 'Other')], null=False, blank=False)

    def __str__(self):
        return self.name


class Worker(models.Model):
    JOBS = [('Doctor', 'Doctor'),
            ('Nurse', 'Nurse')]
    Person = models.ForeignKey(to=Person, on_delete=models.CASCADE,
                               related_name='worker_person',
                               default='',
                               null=False,
                               blank=False)
    role = models.CharField(max_length=50, choices=JOBS, default='Doctor', null=False, blank=False)
    department = models.ForeignKey(to=Department, on_delete=models.CASCADE,
                                   related_name='worker_department',
                                   default='',
                                   null=False,
                                   blank=False)

    def __str__(self):
        return "class {} - {} {} works in {} {}".format(type(self).__name__, self.role, self.Person, self.department,
                                                        self.department.hospital)


class Patient(models.Model):
    Person = models.ForeignKey(to=Person, on_delete=models.CASCADE,
                               related_name='patient_person',
                               default='',
                               null=False,
                               blank=False)
    department_in = models.ForeignKey(to=Department, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return "class {} - {} in {}".format(type(self).__name__, self.Person, self.department_in)


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
    worker = models.ForeignKey(to=Worker, on_delete=models.CASCADE, null=False, blank=False)
    patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE, null=False, blank=False)
    result = models.CharField(max_length=20, choices=RESULTS, default=HEALTY, null=False, blank=False)

    def __str__(self):
        return "class {} - date: {} exam result {}".format(type(self).__name__, self.date,
                                                           self.result)
