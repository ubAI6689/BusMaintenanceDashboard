# Generated by Django 3.2.16 on 2023-09-17 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DST_CANPERIODHIST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('APPLY_DT', models.CharField(max_length=255, verbose_name='')),
                ('DEPOT_ID', models.CharField(max_length=255, verbose_name='Unique name code for every depot')),
                ('DEPOT_NM', models.CharField(max_length=255, verbose_name='')),
                ('VEH_TPCD', models.IntegerField(verbose_name='')),
                ('VEH_TPNM', models.CharField(max_length=255, verbose_name='')),
                ('VEH_ID', models.CharField(max_length=255, verbose_name='')),
                ('EVT_DATETIME', models.CharField(max_length=255, verbose_name='')),
                ('SPN_513', models.FloatField(verbose_name='Actual Engine - Percent Torque')),
                ('SPN_190', models.FloatField(verbose_name='Engine Speed')),
                ('SPN_91', models.FloatField(verbose_name='Accelerator Pedal Position 1')),
                ('SPN_92', models.FloatField(verbose_name='Engine Percent Load At Current Speed')),
                ('SPN_524', models.FloatField(verbose_name='Transmission Selected Gear')),
                ('SPN_523', models.FloatField(verbose_name='Transmission Current Gear')),
                ('SPN_1821', models.CharField(max_length=255, verbose_name='Position of doors')),
                ('SPN_2806', models.FloatField(verbose_name='FMS-standard SW-version supported.')),
                ('SPN_1087', models.FloatField(verbose_name='Service Brake Circuit 1 Air Pressure')),
                ('SPN_1088', models.FloatField(verbose_name='Service Brake Circuit 2 Air Pressure')),
                ('SPN_917', models.FloatField(verbose_name='High Resolution Total Vehicle Distance')),
                ('SPN_247', models.FloatField(verbose_name='Engine Total Hours of Operation')),
                ('SPN_964', models.FloatField(verbose_name='Represent Time / Date')),
                ('SPN_250', models.FloatField(verbose_name='Engine Total Fuel Used')),
                ('SPN_237', models.FloatField(verbose_name='Vehicle Identification Number')),
                ('SPN_110', models.FloatField(verbose_name='Engine Coolant Temperature')),
                ('SPN_84', models.FloatField(verbose_name='Wheel-Based Vehicle Speed')),
                ('SPN_597', models.CharField(max_length=255, verbose_name='Brake Switch')),
                ('SPN_595', models.FloatField(verbose_name='Cruise Control Active')),
                ('SPN_183', models.FloatField(verbose_name='Engine Fuel Rate')),
                ('SPN_184', models.FloatField(verbose_name='Engine Instantaneous Fuel Economy')),
                ('SPN_171', models.FloatField(verbose_name='Ambient Air Temperature')),
                ('SPN_96', models.FloatField(verbose_name='Fuel Level 1')),
                ('MODEL_NUM', models.CharField(max_length=255, verbose_name='')),
            ],
        ),
    ]