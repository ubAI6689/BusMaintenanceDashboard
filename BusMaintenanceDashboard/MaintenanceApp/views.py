import csv
import json
import numpy as np
import datetime
import pytz
utc=pytz.UTC
import pandas as pd
from django.http import JsonResponse
from django.apps import apps
from django.shortcuts import render
from django.core import serializers
from django.db.models import F
from .models import DST_CANPERIODHIST, FORECAST, PROCESSED

def dashboard_view(request):
    return render(request, 'dashboard.html')

def buses_view(request):
    return render(request, 'bus_list.html')

def canbus_data_view(request):
    return render(request, 'canbus_data.html')

def get_canbus_data(request):
    csv_file_path = "/home/abu/data/depot.csv"
    with open(csv_file_path, 'r') as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        data = [row for row in reader]
    
    return JsonResponse({'header': header, 'data': data})

def echart_demo(request):
    return render(request, 'echart_demo.html')

def get_database_data(request):
    vehicle_id = request.GET.get('vehicle_id', None)
    print("Debug: Received Vehicle ID: ", vehicle_id)

    queryset = DST_CANPERIODHIST.objects.all()

    if vehicle_id:
        queryset = queryset.filter(VEH_ID=vehicle_id)

    queryset = queryset.values(
        'APPLY_DT', 'DEPOT_ID', 'DEPOT_NM', 'SPN_190', 'SPN_513', 'SPN_524', 'SPN_523'
    )[:100]  # Limit to first 100 records and selected fields

    data_list = list(queryset)
    verbose_names = {f.name: f.verbose_name for f in DST_CANPERIODHIST._meta.fields if f.name in ['APPLY_DT', 'DEPOT_ID', 'DEPOT_NM', 'SPN_190', 'SPN_513', 'SPN_524', 'SPN_523']}

    return JsonResponse({"header": ['APPLY_DT', 'DEPOT_ID', 'DEPOT_NM', 'SPN_190', 'SPN_513', 'SPN_524', 'SPN_523'], "data": data_list, "verbose_names": verbose_names})

def get_all_vehicle_ids(request):
    vehicle_ids = DST_CANPERIODHIST.objects.values_list('VEH_ID', flat=True).distinct()
    return JsonResponse({"vehicle_ids": list(vehicle_ids)})

def spn_110_plot(request):
    return render(request, 'spn_110_plot.html')

def get_spn_110_data(request):
    vehicle_id = request.GET.get('vehicle_id', None)
    queryset = DST_CANPERIODHIST.objects.filter(VEH_ID=vehicle_id).order_by('EVT_DATETIME').values('SPN_110', 'EVT_DATETIME')
    # data_list = list(queryset)
    # print("Debug: Sending data:", data_list)  # Debug log
    spn_110_data = [entry['SPN_110'] for entry in queryset]
    evt_datetime_data = [entry['EVT_DATETIME'] for entry in queryset]
    return JsonResponse({"spn_110_data": spn_110_data, "evt_datetime_data": evt_datetime_data})

def get_all_spn_fields(request):
    model = apps.get_model('MaintenanceApp', 'DST_CANPERIODHIST')
    spn_fields = [field.name for field in model._meta.fields if 'SPN' in field.name]
    return JsonResponse({"spn_fields": spn_fields})

def plot_dynamic_data(request):
    return render(request, 'dynamic_chart.html')

def get_dynamic_data(request):
    vehicle_id = request.GET.get('vehicle_id', None)
    param = request.GET.get('param', None)  # Just one param
    
    print(f"Debug - Received request with Vehicle ID: {vehicle_id}, Param: {param}")  # Backend log

    if not vehicle_id or not param:
        return JsonResponse({'error': 'Invalid parameters'}, status=400)
    
    queryset = DST_CANPERIODHIST.objects.filter(VEH_ID=vehicle_id).values('EVT_DATETIME', param)
    
    # Sort the queryset based on 'EVT_DATETIME'
    sorted_data = sorted(list(queryset), key=lambda x: x['EVT_DATETIME'])
    
    param_data = [entry[param] for entry in sorted_data]
    datetime_data = [entry['EVT_DATETIME'] for entry in sorted_data]
    
    response_data = {
        'param_data': param_data,
        'datetime_data': datetime_data
    }

    print(response_data)  # Backend log
    return JsonResponse(response_data)

def plot_forecast(request):
    return render(request, 'plot_forecast.html')

def get_forecast_and_processed_data(request):
    vehicle_id = request.GET.get('vehicle_id', None)
    param = request.GET.get('param', None)

    print(f"Get request - vehicle ID: {vehicle_id}, param: {param}")

    if not vehicle_id or not param:
        return JsonResponse({'error': 'Invalid parameters'}, status=400)

    # Query from PROCESSED model
    queryset_processed = PROCESSED.objects.filter(VEH_ID=vehicle_id).values('EVT_DATETIME', param)
    dtp = [entry['EVT_DATETIME'] for entry in queryset_processed]
    pp = [entry[param] for entry in queryset_processed]

    # Query from FORECAST model
    queryset_forecast = FORECAST.objects.filter(VEH_ID=vehicle_id).values('forecast_dt', f"{param}_fc")
    dtf = [entry['forecast_dt'] for entry in queryset_forecast]
    pf = [entry[f"{param}_fc"] for entry in queryset_forecast]

    start_dt = pd.to_datetime('2023-04-30 10:00').tz_localize('UTC')
    current_dt = pd.to_datetime('2023-04-30 14:00').tz_localize('UTC')
    end_dt = pd.to_datetime('2023-04-30 20:00').tz_localize('UTC')
    dfp = pd.DataFrame({'datetime':dtp, 'pp':pp}).sort_values('datetime')
    dff = pd.DataFrame({'datetime':dtf, 'pf':pf}).sort_values('datetime')
    df = pd.merge(dfp,dff,on='datetime').sort_values('datetime')
    df = df[ (df['datetime']>=start_dt) & (df['datetime']<end_dt)].fillna('nan')
    
    df.loc[df['datetime'] >= current_dt, 'pp'] = 'nan'


    print(df[df['datetime']>=current_dt]['pp'].unique())
    # df[df['datetime']>=current_dt]['pp'] = 'nan'

    pp = df['pp'].tolist()
    pf = df['pf'].tolist()
    dt = df['datetime'].tolist()
    dt = [x.strftime('%Y-%m-%d %H:%M:%S') for x in dt]

    print(dt[:10], len(dt))
    print(pp[:10], len(pp))
    print(pf[:10], len(pf))
    
    response_data = {
        'param_data_processed': pp,
        # 'datetime_data_processed': dtp,
        'param_data_forecast': pf,
        'datetime_data_forecast': dt,
    }
    
    return JsonResponse(response_data)


def get_all_vehicle_ids_forecast(request):
    vehicle_ids = FORECAST.objects.values_list('VEH_ID', flat=True).distinct()
    return JsonResponse({"vehicle_ids": list(vehicle_ids)})

def bus_info(request):
    bus_data = FORECAST.objects.values_list('VEH_ID', flat=True).distinct()
    return render(request, 'bus_info.html', {'buses': bus_data})

