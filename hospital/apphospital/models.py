# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Hospital(models.Model):
    name = models.CharField(db_index=True, max_length=200, null=False, blank=False)
    city = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return "ID{} - {}".format(self.pk, self.name)


class HospitalDepartment(models.Model):
    hospital = models.ForeignKey(to=Hospital, on_delete=models.CASCADE,
                                 related_name='departments',
                                 null=False,
                                 blank=False)
    name = models.CharField(db_index=True, max_length=200, null=False, blank=False)

    def __str__(self):
        return "{}".format(self.name)


class HospitalPerson(models.Model):
    GENDER_MALE = 'MALE'
    GENDER_FEMALE = 'FEMALE'
    GENDER_OTHER = 'OTHER'
    GENDER_CHOICES = [(GENDER_MALE, GENDER_MALE), (GENDER_FEMALE, GENDER_FEMALE), (GENDER_OTHER, GENDER_OTHER)]
    name = models.CharField(db_index=True, max_length=200, null=False, blank=False)
    age = models.PositiveSmallIntegerField(default=0, null=False, blank=True)
    gender = models.CharField(max_length=200, choices=GENDER_CHOICES, null=False, blank=False)

    def __str__(self):
        return self.name


class HospitalWorker(models.Model):
    JOBS = [('Doctor', 'Doctor'),
            ('Nurse', 'Nurse')]
    Person = models.ForeignKey(to=HospitalPerson, on_delete=models.CASCADE,
                               related_name='department_worker',
                               null=False,
                               blank=False)
    role = models.CharField(max_length=50, choices=JOBS, null=False, blank=False)
    department = models.ForeignKey(to=HospitalDepartment, on_delete=models.CASCADE,
                                   related_name='department_worker',
                                   null=False,
                                   blank=False)

    def __str__(self):
        return "<{class_name} - {role} {name} works in {department} {hospital}>".format(
            class_name=self.__class__.__name__,
            role=self.role,
            name=self.Person,
            department=self.department,
            hospital=self.department.hospital,
        )


class HospitalPatient(models.Model):
    Person = models.ForeignKey(to=HospitalPerson, on_delete=models.CASCADE,
                               related_name='person_patient',
                               null=False,
                               blank=False)
    department_in = models.ForeignKey(to=HospitalDepartment, on_delete=models.CASCADE, related_name='person_department',
                                      null=False, blank=False)

    def __str__(self):
        return "<{class_name} - {name} hospitalized in {department} {hospital}>".format(
            class_name=self.__class__.__name__, name=self.Person, department=self.department_in,
            hospital=self.department_in.hospital)


class MedicalExamination(models.Model):
    MEDICAL_EXAMINATION_HEALTHY = 'healthy'
    MEDICAL_EXAMINATION_CORONA = 'Corona'
    MEDICAL_EXAMINATION_BOTISM = 'Botism'
    MEDICAL_EXAMINATION_DEAD = 'Dead'
    RESULTS = [(MEDICAL_EXAMINATION_HEALTHY, MEDICAL_EXAMINATION_HEALTHY),
               (MEDICAL_EXAMINATION_CORONA, MEDICAL_EXAMINATION_CORONA),
               (MEDICAL_EXAMINATION_BOTISM, MEDICAL_EXAMINATION_BOTISM),
               (MEDICAL_EXAMINATION_DEAD, MEDICAL_EXAMINATION_DEAD)]
    date = models.DateTimeField("exam date", auto_now=False, auto_now_add=False)
    worker = models.ForeignKey(to=HospitalWorker, on_delete=models.CASCADE, null=False, blank=False)
    patient = models.ForeignKey(to=HospitalPatient, on_delete=models.CASCADE, null=False, blank=False)
    result = models.CharField(max_length=20, choices=RESULTS, default=MEDICAL_EXAMINATION_HEALTHY, null=False,
                              blank=False)

    def __str__(self):
        return "{class_name} - Patient {patient_name} tested by {worker_name} in  date: {date}. The exam result" \
               " {exam_result}".format(class_name=self.__class__.__name__,
                                       patient_name=self.patient,
                                       worker_name=self.worker,
                                       date=self.date,
                                       exam_result=self.result)
