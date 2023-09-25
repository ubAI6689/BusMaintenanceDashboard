from django.core.management.base import BaseCommand
from MaintenanceApp.models import ParameterThreshold

class Command(BaseCommand):
    help = 'Populates the ParameterThreshold model with initial data'

    def handle(self, *args, **kwargs):
        # Define your initial data
        initial_data = {
            'SPN_110': [-40, 210],
            'SPN_183': [0, 3212.75],
            'SPN_184': [0, 125.5],
            'SPN_84': [0, 250.99609375],
            'SPN_190': [0, 8031.88],
            'SPN_96': [0, 100],
            'SPN_91': [0, 100],
        }

        # Populate the model
        for param, values in initial_data.items():
            min_val, max_val = values
            ParameterThreshold.objects.update_or_create(
                parameter_name=param,
                defaults={'min_value': min_val, 'max_value': max_val},
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated ParameterThreshold'))
