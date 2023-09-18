# to load the data into postgresql
# run inside django shell
# $ python3 manage.py shell
# $ exec(open('/path/to/this/script.py')).read()

import pandas as pd
import django

django.setup()
from MaintenanceApp.models import DST_CANPERIODHIST

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

# Load the .pkl file into a DataFrame
df = pd.read_pickle('/home/abu/data/DST_CANPERIODHIST_202301.pkl')

# Get existing primary keys from the database (replace 'id' with your primary key field)
existing_pks = set(DST_CANPERIODHIST.objects.values_list('id', flat=True))

# Loop through DataFrame in chunks, create model instances, and bulk insert
batch_size = 1000
for chunk in chunker(df, batch_size):
    model_instances = []
    for _, row in chunk.iterrows():
        instance = DST_CANPERIODHIST()
        for field, value in row.items():
            setattr(instance, field, value)
        if instance.pk not in existing_pks:
            model_instances.append(instance)
    DST_CANPERIODHIST.objects.bulk_create(model_instances)
