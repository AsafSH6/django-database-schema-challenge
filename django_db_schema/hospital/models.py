# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Department(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Worker(Person):
    departments = models.ManyToManyField(Department)
    position = models.CharField(max_length=1, choices=[('D', 'Doctor'), ('N', 'Nurse')])


class Patient(Person):
    pass


class ExaminationResult(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    time = models.DateTimeField()
    examiner = models.ForeignKey(Worker, on_delete=models.CASCADE)
    result = models.CharField(max_length=1, choices=[('H', 'Healthy'), ('C', 'Corona'), ('B', 'Botism'), ('D', 'Dead')])

    def __str__(self):
        return "%s %s" % (self.patient.name, str(self.time.strftime("%d-%m-%Y %H:%M")))
