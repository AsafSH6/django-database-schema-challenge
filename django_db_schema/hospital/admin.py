# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Hospital, Worker, Patient, Department, ExaminationResult

# Register your models here.
admin.site.register(Hospital)
admin.site.register(Worker)
admin.site.register(Patient)
admin.site.register(Department)
admin.site.register(ExaminationResult)
