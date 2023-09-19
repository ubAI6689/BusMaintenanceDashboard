# to load the data into postgresql
# run inside django shell
# $ python3 manage.py shell
# $ exec(open('/path/to/this/script.py')).read()

import pandas as pd
import django

django.setup()
from MaintenanceApp.models import FORECAST

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

# Load the .pkl file into a DataFrame

files = [
    '/home/abu/BusMaintenanceAnalysis/latest_forecasts/fc_VAG8541.pkl',
    '/home/abu/BusMaintenanceAnalysis/latest_forecasts/fc_VAE7038.pkl',
    '/home/abu/BusMaintenanceAnalysis/latest_forecasts/fc_VH4236.pkl']
df = pd.concat([pd.read_pickle(f) for f in files])

# Get existing primary keys from the database (replace 'id' with your primary key field)
existing_pks = set(FORECAST.objects.values_list('id', flat=True))

# Loop through DataFrame in chunks, create model instances, and bulk insert
batch_size = 1000
for chunk in chunker(df, batch_size):
    model_instances = []
    for _, row in chunk.iterrows():
        instance = FORECAST()
        for field, value in row.items():
            setattr(instance, field, value)
        if instance.pk not in existing_pks:
            model_instances.append(instance)
    FORECAST.objects.bulk_create(model_instances)
