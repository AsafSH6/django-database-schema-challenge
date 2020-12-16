# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Hospital, HospitalWorker, Patient, Department, \
    ExaminationResult, Person

# Register your models here.
admin.site.register(Hospital)
admin.site.register(HospitalWorker)
admin.site.register(Patient)
admin.site.register(Department)
admin.site.register(ExaminationResult)
admin.site.register(Person)
