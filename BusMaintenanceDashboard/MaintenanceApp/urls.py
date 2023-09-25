from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    # path('', views.dashboard_view, name='dashboard'),
    path('', RedirectView.as_view(url='bus_info/'), name='redirect-to-bus_info'),
    path('bus_info/', views.alarm_info_view, name='bus_info'),
    # path('buses/', views.buses_view, name='buses'),
    path('canbus_data/', views.canbus_data_view, name='canbus_data'),
    path('get_canbus_data/', views.get_canbus_data, name='get_canbus_data'),
    path('echart_demo/', views.echart_demo, name='echart_demo'),
    path('get_database_data/', views.get_database_data, name='get_database_data'),
    path('get_all_vehicle_ids/', views.get_all_vehicle_ids, name='get_all_vehicle_ids'),
    path('spn_110_plot/', views.spn_110_plot, name='spn_110_plot'),
    path('get_spn_110_data/', views.get_spn_110_data, name='get_spn_110_data'),
    path('get_all_spn_fields/', views.get_all_spn_fields, name='get_all_spn_fields'),
    path('plot_dynamic_data/', views.plot_dynamic_data, name='plot_dynamic_data'),
    path('get_dynamic_data/', views.get_dynamic_data, name='get_dynamic_data'),
    path('plot_forecast/', views.plot_forecast, name='plot_forecast'),
    path('get_forecast_and_processed_data/', views.get_forecast_and_processed_data, name='get_forecast_and_processed_data'),
    path('get_all_vehicle_ids_forecast/', views.get_all_vehicle_ids_forecast, name='get_all_vehicle_ids_forecast'),
    path('bus_info/', views.bus_info, name='bus_info'),
    path('get_threshold_data/', views.get_threshold_data, name='get_threshold_data'),
]
