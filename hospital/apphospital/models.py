# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models


class Hospital(models.Model):
    hospital_id = models.AutoField(primary_key=True)
    hospital_name = models.CharField(max_length=200)
    hospital_city = models.CharField(max_length=200, null=True)

    def __str__(self):
        return "ID: {} - {}".format(self.hospital_id, self.hospital_name)


class Department(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=200)

    def __str__(self):
        return "ID: {} - department {} in {}".format(self.department_id, self.department_name, self.hospital)


class People(models.Model):
    GENDER_TYPES = [('M', 'Male'),
                    ('F', 'Female'),
                    ('Other', 'Other')]
    people_id = models.AutoField(primary_key=True)
    people_name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    gender = models.CharField(max_length=200, choices=GENDER_TYPES, default="Male")

    def __str__(self):
        return self.people_name


class Worker(People):
    JOBS = [('Doc', 'Doctor'),
            ('Nur', 'Nurse')]
    role = models.CharField(max_length=50, choices=JOBS, default='Doctor')
    department = models.ManyToManyField(Department)

    def __str__(self):
        return "{} {} works in {}".format(self.role, self.people_name, self.department)


class Patient(People):
    department_in = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.people_name, self.department_in)


class MedicalExamination(models.Model):
    HEALTY = 'Healty'
    CORONA = 'CORONA'
    BOTISM = 'BOTISM'
    DEAD = 'DEAD'
    RESULTS = [(HEALTY, HEALTY),
               (CORONA, CORONA),
               (BOTISM, BOTISM),
               (DEAD, DEAD)]
    examination_date = models.DateTimeField("exam date")
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    examination_result = models.CharField(max_length=20, choices=RESULTS, default=HEALTY)

    def __str__(self):
        return "date: {} worker: {} patient: {} exam result {}".format(self.examination_date, self.worker, self.patient,
                                                                       self.examination_result)
