# In admin.py
from django.contrib import admin
from .models import ParameterThreshold

@admin.register(ParameterThreshold)
class ParameterThresholdAdmin(admin.ModelAdmin):
    list_display = ('parameter_name', 'min_value', 'max_value')
