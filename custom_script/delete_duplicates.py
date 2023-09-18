from django.db.models import Count
from MaintenanceApp.models import DST_CANPERIODHIST

# Find duplicate records
duplicate_rows = DST_CANPERIODHIST.objects.values('VEH_ID', 'EVT_DATETIME')\
    .annotate(count=Count('id'))\
    .values('VEH_ID', 'EVT_DATETIME', 'count')\
    .filter(count__gt=1)

# Initialize counter for deleted duplicates
deleted_count = 0

# Loop through the duplicate records and delete
for duplicate_row in duplicate_rows:
    duplicate_data = DST_CANPERIODHIST.objects.filter(
        VEH_ID=duplicate_row['VEH_ID'],
        EVT_DATETIME=duplicate_row['EVT_DATETIME']
    ).exclude(id=min(DST_CANPERIODHIST.objects.filter(
        VEH_ID=duplicate_row['VEH_ID'],
        EVT_DATETIME=duplicate_row['EVT_DATETIME']
    ).values_list('id', flat=True)))
    
    # Print each duplicate found
    print(f"Found duplicate for VEH_ID {duplicate_row['VEH_ID']} at {duplicate_row['EVT_DATETIME']}. Deleting...")

    # Delete the duplicates and print
    deleted_count += duplicate_data.delete()[0]

print(f"Deleted {deleted_count} duplicate rows.")
