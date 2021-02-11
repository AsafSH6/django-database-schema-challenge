# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import (Person, Patient, Hospital, HospitalWorker, Department,
                    Examination)

admin.register(Person)
admin.register(Patient)
admin.register(Hospital)
admin.register(Department)
admin.register(Examination)
admin.register(HospitalWorker)
