# Generated by Django 2.0.3 on 2018-03-30 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Scanning_MSGs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CdIe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_ie_criticalitydiagnostics', models.IntegerField(blank=True, db_column='FK_IE_criticalityDiagnostics', null=True)),
                ('ie_id', models.IntegerField(blank=True, db_column='IE_ID', null=True)),
                ('ie_criticality', models.CharField(blank=True, db_column='IE_criticality', max_length=20, null=True)),
                ('typeoferror', models.CharField(blank=True, db_column='TypeOfError', max_length=255, null=True)),
            ],
            options={
                'db_table': 'CD_IE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CriticalityDiagnostics3G',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.IntegerField(blank=True, db_column='SN', null=True)),
                ('error_indication', models.IntegerField(blank=True, null=True)),
                ('procedurecode', models.IntegerField(blank=True, db_column='ProcedureCode', null=True)),
                ('triggeringmessage', models.CharField(blank=True, db_column='TriggeringMessage', max_length=255, null=True)),
                ('procedurecriticality', models.CharField(blank=True, db_column='ProcedureCriticality', max_length=255, null=True)),
                ('ie_id', models.IntegerField(blank=True, db_column='IE_ID', null=True)),
                ('ie_criticality', models.CharField(blank=True, db_column='IE_Criticality', max_length=255, null=True)),
                ('repitionnumber', models.IntegerField(blank=True, db_column='RepitionNumber', null=True)),
            ],
            options={
                'db_table': 'criticality_diagnostics_3G',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FailureList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.IntegerField(blank=True, db_column='SN', null=True)),
                ('plmnidentity', models.TextField(blank=True, db_column='PLMNidentity', null=True)),
                ('lac', models.TextField(blank=True, null=True)),
                ('sac', models.TextField(blank=True, null=True)),
                ('cause', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'failure_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NumberOfBroadcastsCompleted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.IntegerField(blank=True, db_column='SN', null=True)),
                ('plmnidentity', models.TextField(blank=True, db_column='PLMNidentity', null=True)),
                ('lac', models.TextField(blank=True, null=True)),
                ('sac', models.TextField(blank=True, null=True)),
                ('number_broadcasts_completed', models.IntegerField(blank=True, db_column='Number_Broadcasts_Completed', null=True)),
                ('number_broadcasts_completed_info', models.CharField(blank=True, db_column='Number_Broadcasts_Completed_Info', max_length=255, null=True)),
            ],
            options={
                'db_table': 'Number_Of_Broadcasts_Completed',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RadioResourceLoadingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.IntegerField(blank=True, db_column='SN', null=True)),
                ('plmnidentity', models.TextField(blank=True, db_column='PLMNidentity', null=True)),
                ('lac', models.TextField(blank=True, null=True)),
                ('sac', models.TextField(blank=True, null=True)),
                ('availablebandwidth', models.IntegerField(blank=True, db_column='AvailableBandwidth', null=True)),
            ],
            options={
                'db_table': 'radio_resource_loading_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceAreasList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.IntegerField(blank=True, db_column='SN', null=True)),
                ('sn_response', models.IntegerField(blank=True, db_column='SN_response', null=True)),
                ('sn_indication', models.IntegerField(blank=True, db_column='SN_indication', null=True)),
                ('plmnidentity', models.TextField(blank=True, db_column='PLMNidentity', null=True)),
                ('sac', models.TextField(blank=True, null=True)),
                ('lac', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Service_Areas_List',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TaiCoordinates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(blank=True, max_length=255, null=True)),
                ('longtitude', models.CharField(blank=True, max_length=255, null=True)),
                ('reference', models.IntegerField(blank=True, null=True)),
                ('flag', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'TAI_Coordinates',
                'managed': False,
            },
        ),
    ]
