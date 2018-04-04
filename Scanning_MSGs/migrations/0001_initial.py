# Generated by Django 2.0.3 on 2018-03-30 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssignmentMsgColumns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_content', models.CharField(db_column='Msg_Content', max_length=70)),
                ('rep_per', models.IntegerField(db_column='Rep_per')),
                ('mas_id', models.CharField(db_column='mas_ID', max_length=70)),
                ('datacoding_scheme', models.IntegerField(db_column='DataCoding_Scheme')),
                ('endtime', models.CharField(db_column='EndTime', max_length=70)),
                ('starttime', models.CharField(db_column='StartTime', max_length=70)),
            ],
            options={
                'managed': False,
                'db_table': 'Assignment_msg_columns',
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'managed': False,
                'db_table': 'auth_group',
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'managed': False,
                'db_table': 'auth_group_permissions',
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'managed': False,
                'db_table': 'auth_permission',
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'auth_user',
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'managed': False,
                'db_table': 'auth_user_groups',
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'managed': False,
                'db_table': 'auth_user_user_permissions',
            },
        ),
        migrations.CreateModel(
            name='BroadcastCancelledAreaList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idbroadcast_cancelled_area_list', models.IntegerField(blank=True, null=True)),
                ('cell_id_cancelled_list', models.IntegerField(blank=True, null=True)),
                ('tai_cancelled_list', models.IntegerField(blank=True, db_column='TAI_cancelled_list', null=True)),
                ('emergencyareaid_cancelled_list', models.IntegerField(blank=True, db_column='EmergencyAreaID_cancelled_list', null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'broadcast_cancelled_area_list',
            },
        ),
        migrations.CreateModel(
            name='BroadcastScheduledAreaList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idbroadcast_scheduled_area_list', models.IntegerField(blank=True, null=True)),
                ('cell_id_broadcast_list', models.IntegerField(blank=True, null=True)),
                ('tai_broadcast_list', models.IntegerField(blank=True, db_column='TAI_broadcast_list', null=True)),
                ('emergencyareaid_broadcast_list', models.IntegerField(blank=True, db_column='EmergencyAreaID_broadcast_list', null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'broadcast_scheduled_area_list',
            },
        ),
        migrations.CreateModel(
            name='CriticalityDiagnostics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idcriticality_diagnostics', models.CharField(blank=True, max_length=1, null=True)),
                ('procedurecode', models.CharField(blank=True, max_length=1, null=True)),
                ('triggeringmessage', models.CharField(blank=True, max_length=1, null=True)),
                ('procedurecriticality', models.CharField(blank=True, max_length=1, null=True)),
                ('ie_criticalitydiagnostics', models.CharField(blank=True, db_column='IE_criticalitydiagnostics', max_length=1, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'criticality_diagnostics',
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'managed': False,
                'db_table': 'django_admin_log',
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'managed': False,
                'db_table': 'django_content_type',
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'django_migrations',
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'django_session',
            },
        ),
        migrations.CreateModel(
            name='EaiList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_ie32', models.CharField(blank=True, db_column='FK_IE32', max_length=1, null=True)),
                ('fk_eaid_broadcast_list', models.IntegerField(blank=True, db_column='FK_EAID_broadcast_list', null=True)),
                ('fk_eaid_cancelled_list', models.CharField(blank=True, db_column='FK_EAID_cancelled_list', max_length=1, null=True)),
                ('fk_emergency_area_id_list', models.CharField(blank=True, db_column='Fk_emergency_area_id_list', max_length=1, null=True)),
                ('ecgi_list_fromeai', models.IntegerField(blank=True, db_column='eCGI_list_fromEAI', null=True)),
                ('eaid', models.TextField(blank=True, db_column='EAid', null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'EAI_list',
            },
        ),
        migrations.CreateModel(
            name='EcgiList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_ie30', models.CharField(blank=True, db_column='FK_IE30', max_length=255, null=True)),
                ('fk_ie33', models.CharField(blank=True, db_column='FK_IE33', max_length=1, null=True)),
                ('fk_cell_id_broadcast_list', models.CharField(blank=True, db_column='FK_cell_id_broadcast_list', max_length=255, null=True)),
                ('fk_cell_id_cancelled_list', models.CharField(blank=True, db_column='FK_cell_id_cancelled_list', max_length=255, null=True)),
                ('fk_eaid_cancelled_list', models.CharField(blank=True, db_column='FK_EAID_cancelled_list', max_length=1, null=True)),
                ('fk_ecgi_list_tai', models.IntegerField(blank=True, db_column='FK_eCGI_list_TAI', null=True)),
                ('fk_cell_id_list', models.CharField(blank=True, db_column='FK_cell_id_list', max_length=1, null=True)),
                ('fk_ecgi_list_eai', models.IntegerField(blank=True, db_column='FK_eCGI_list_EAI', null=True)),
                ('plmnidentity', models.TextField(blank=True, db_column='PLMNidentity', null=True)),
                ('cell_id', models.CharField(blank=True, max_length=255, null=True)),
                ('noofbroadcast', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'eCGI_list',
            },
        ),
        migrations.CreateModel(
            name='GeiList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_ie29', models.IntegerField(blank=True, db_column='FK_IE29', null=True)),
                ('fk_ie28', models.IntegerField(blank=True, db_column='FK_IE28', null=True)),
                ('plmnidentity', models.TextField(blank=True, db_column='PLMNidentity', null=True)),
                ('enb_id', models.TextField(blank=True, db_column='ENB_ID', null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'GEI_list',
            },
        ),
        migrations.CreateModel(
            name='ListofEcgi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_tai_broadcast_list', models.IntegerField(blank=True, db_column='FK_TAI_broadcast_list', null=True)),
                ('fk_eaid_broadcast_list', models.IntegerField(blank=True, db_column='FK_EAID_broadcast_list', null=True)),
                ('fk_cell_id_cancelled_list', models.IntegerField(blank=True, db_column='FK_cell_id_cancelled_list', null=True)),
                ('fk_eaid_cancelled_list', models.IntegerField(blank=True, db_column='FK_EAID_cancelled_list', null=True)),
                ('ecgi_list', models.IntegerField(blank=True, db_column='eCGI_list', null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'listof_eCGI',
            },
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_status', models.CharField(blank=True, max_length=1, null=True)),
                ('msg_generation', models.CharField(blank=True, max_length=1, null=True)),
                ('sn_indication', models.IntegerField(blank=True, db_column='SN_indication', null=True)),
                ('serial_number', models.CharField(max_length=255)),
                ('new_serial_number', models.CharField(blank=True, max_length=1, null=True)),
                ('old_serial_number', models.CharField(blank=True, max_length=1, null=True)),
                ('broadcast_message_content', models.CharField(blank=True, max_length=1, null=True)),
                ('message_identifier', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.CharField(blank=True, max_length=1, null=True)),
                ('list_of_tais', models.CharField(blank=True, db_column='list_of_TAIs', max_length=1, null=True)),
                ('warning_area_list', models.CharField(blank=True, max_length=1, null=True)),
                ('repetition_period', models.CharField(blank=True, max_length=70, null=True)),
                ('extended_repetition_period', models.CharField(blank=True, max_length=70, null=True)),
                ('number_of_broadcasts_requested', models.CharField(blank=True, max_length=1, null=True)),
                ('messagetype', models.CharField(blank=True, max_length=255, null=True)),
                ('warning_security_information', models.CharField(blank=True, max_length=1, null=True)),
                ('data_coding_scheme', models.CharField(blank=True, max_length=1, null=True)),
                ('warning_message_content', models.CharField(blank=True, max_length=1, null=True)),
                ('omc_id', models.CharField(blank=True, max_length=1, null=True)),
                ('concurrent_warning_message_indicator', models.CharField(blank=True, max_length=1, null=True)),
                ('send_write_replace_warning_indication', models.CharField(blank=True, max_length=10, null=True)),
                ('global_enb_id', models.CharField(blank=True, max_length=1, null=True)),
                ('send_stop_warning_indication', models.CharField(blank=True, max_length=1, null=True)),
                ('stop_all_indicator', models.CharField(blank=True, max_length=1, null=True)),
                ('paging_etws_indicator', models.CharField(blank=True, max_length=1, null=True)),
                ('message_structure', models.CharField(blank=True, max_length=1, null=True)),
                ('warning_type', models.CharField(blank=True, max_length=1, null=True)),
                ('broadcast_message_content_validity_indicator', models.CharField(blank=True, max_length=1, null=True)),
                ('emergency_indicator', models.CharField(blank=True, max_length=1, null=True)),
                ('channel_indicator', models.CharField(blank=True, max_length=1, null=True)),
                ('number_of_pages', models.CharField(blank=True, max_length=1, null=True)),
                ('schedule_period', models.CharField(blank=True, max_length=1, null=True)),
                ('number_of_reserved_slots', models.CharField(blank=True, max_length=1, null=True)),
                ('broadcast_message_type', models.CharField(blank=True, max_length=1, null=True)),
                ('warning_period', models.CharField(blank=True, max_length=1, null=True)),
                ('length_indicator', models.CharField(blank=True, max_length=1, null=True)),
                ('keep_alive_repetition_period', models.CharField(blank=True, max_length=1, null=True)),
                ('cause', models.CharField(blank=True, max_length=1, null=True)),
                ('criticality_diagnostics', models.CharField(blank=True, max_length=1, null=True)),
                ('warning_securityinfo', models.CharField(blank=True, max_length=1, null=True)),
                ('broadcast_scheduled_area_list', models.CharField(blank=True, max_length=1, null=True)),
                ('broadcast_cancelled_area_list', models.CharField(blank=True, max_length=1, null=True)),
                ('broadcast_empty_area_list', models.CharField(blank=True, max_length=1, null=True)),
                ('restarted_cell_list', models.IntegerField(blank=True, null=True)),
                ('list_of_tais_restart', models.CharField(blank=True, db_column='list_of_TAIs_restart', max_length=1, null=True)),
                ('list_of_eais_restart', models.CharField(blank=True, db_column='list_of_EAIs_restart', max_length=1, null=True)),
                ('failed_cell_list', models.CharField(blank=True, max_length=1, null=True)),
                ('failure_list', models.CharField(blank=True, max_length=1, null=True)),
                ('number_of_broadcasts_completed_list', models.CharField(blank=True, max_length=1, null=True)),
                ('radio_resource_loading_list', models.CharField(blank=True, max_length=1, null=True)),
                ('recovery_indication', models.CharField(blank=True, max_length=1, null=True)),
                ('service_areas_list', models.CharField(blank=True, max_length=1, null=True)),
                ('typeoferror', models.CharField(blank=True, max_length=1, null=True)),
                ('cell_list', models.CharField(blank=True, max_length=1, null=True)),
                ('extras', models.CharField(blank=True, max_length=1, null=True)),
                ('unknown_tracking_area_list', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'Main',
            },
        ),
        migrations.CreateModel(
            name='TaiList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_ie31', models.CharField(blank=True, db_column='Fk_IE31', max_length=255, null=True)),
                ('fk_ie22', models.CharField(blank=True, db_column='FK_IE22', max_length=255, null=True)),
                ('fk_tai_broadcast_list', models.CharField(blank=True, db_column='FK_TAI_broadcast_list', max_length=255, null=True)),
                ('fk_tai_cancelled_list', models.CharField(blank=True, db_column='FK_TAI_cancelled_list', max_length=255, null=True)),
                ('fk_tracking_area_list_for_warning', models.CharField(blank=True, db_column='FK_tracking_area_list_for_warning', max_length=255, null=True)),
                ('ecgi_list_fromtai', models.IntegerField(blank=True, db_column='eCGI_list_fromTAI', null=True)),
                ('plmnidentity', models.TextField(blank=True, db_column='PLMNidentity', null=True)),
                ('tac', models.TextField(blank=True, db_column='TAC', null=True)),
                ('fk_ie30', models.CharField(blank=True, db_column='FK_IE30', max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'TAI_list',
            },
        ),
        migrations.CreateModel(
            name='TAIs_Coordinates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Longitude', models.CharField(max_length=70)),
                ('Latitude', models.CharField(max_length=70)),
                ('Select', models.CharField(max_length=70)),
                ('Referece', models.CharField(max_length=70)),
            ],
            options={
                'managed': False,
                'db_table': 'TAIs_Coordinates',
            },
        ),
        migrations.CreateModel(
            name='WarningAreaList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idwarning_area_list', models.CharField(blank=True, max_length=1, null=True)),
                ('cell_id_list', models.CharField(blank=True, max_length=1, null=True)),
                ('tracking_area_list_for_warning', models.CharField(blank=True, max_length=1, null=True)),
                ('emergency_area_id_list', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'warning_area_list',
            },
        ),
    ]