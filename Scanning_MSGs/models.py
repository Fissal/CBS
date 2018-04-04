# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CdIe(models.Model):
    fk_ie_criticalitydiagnostics = models.IntegerField(db_column='FK_IE_criticalityDiagnostics', blank=True, null=True)  # Field name made lowercase.
    ie_id = models.IntegerField(db_column='IE_ID', blank=True, null=True)  # Field name made lowercase.
    ie_criticality = models.CharField(db_column='IE_criticality', max_length=20, blank=True, null=True)  # Field name made lowercase.
    typeoferror = models.CharField(db_column='TypeOfError', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CD_IE'


class EaiList(models.Model):
    fk_ie32 = models.CharField(db_column='FK_IE32', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fk_eaid_broadcast_list = models.IntegerField(db_column='FK_EAID_broadcast_list', blank=True, null=True)  # Field name made lowercase.
    fk_eaid_cancelled_list = models.CharField(db_column='FK_EAID_cancelled_list', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fk_emergency_area_id_list = models.CharField(db_column='Fk_emergency_area_id_list', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ecgi_list_fromeai = models.IntegerField(db_column='eCGI_list_fromEAI', blank=True, null=True)  # Field name made lowercase.
    eaid = models.TextField(db_column='EAid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EAI_list'


class GeiList(models.Model):
    fk_ie29 = models.IntegerField(db_column='FK_IE29', blank=True, null=True)  # Field name made lowercase.
    fk_ie28 = models.IntegerField(db_column='FK_IE28', blank=True, null=True)  # Field name made lowercase.
    plmnidentity = models.TextField(db_column='PLMNidentity', blank=True, null=True)  # Field name made lowercase.
    enb_id = models.TextField(db_column='ENB_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GEI_list'


class Main(models.Model):
    timestamp = models.DateTimeField(db_column='timeStamp', primary_key=True)  # Field name made lowercase.
    msg_status = models.CharField(max_length=1, blank=True, null=True)
    msg_generation = models.CharField(max_length=1, blank=True, null=True)
    sn_indication = models.IntegerField(db_column='SN_indication', blank=True, null=True)  # Field name made lowercase.
    serial_number = models.CharField(max_length=255)
    new_serial_number = models.CharField(max_length=1, blank=True, null=True)
    old_serial_number = models.CharField(max_length=1, blank=True, null=True)
    broadcast_message_content = models.CharField(max_length=1, blank=True, null=True)
    message_identifier = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=1, blank=True, null=True)
    list_of_tais = models.CharField(db_column='list_of_TAIs', max_length=1, blank=True, null=True)  # Field name made lowercase.
    warning_area_list = models.CharField(max_length=1, blank=True, null=True)
    repetition_period = models.CharField(max_length=1, blank=True, null=True)
    extended_repetition_period = models.CharField(max_length=1, blank=True, null=True)
    number_of_broadcasts_requested = models.CharField(max_length=1, blank=True, null=True)
    messagetype = models.CharField(max_length=255, blank=True, null=True)
    warning_security_information = models.CharField(max_length=1, blank=True, null=True)
    data_coding_scheme = models.CharField(max_length=1, blank=True, null=True)
    warning_message_content = models.CharField(max_length=1, blank=True, null=True)
    omc_id = models.CharField(max_length=1, blank=True, null=True)
    concurrent_warning_message_indicator = models.CharField(max_length=1, blank=True, null=True)
    send_write_replace_warning_indication = models.CharField(max_length=10, blank=True, null=True)
    global_enb_id = models.CharField(max_length=1, blank=True, null=True)
    send_stop_warning_indication = models.CharField(max_length=1, blank=True, null=True)
    stop_all_indicator = models.CharField(max_length=1, blank=True, null=True)
    paging_etws_indicator = models.CharField(max_length=1, blank=True, null=True)
    message_structure = models.CharField(max_length=1, blank=True, null=True)
    warning_type = models.CharField(max_length=1, blank=True, null=True)
    broadcast_message_content_validity_indicator = models.CharField(max_length=1, blank=True, null=True)
    emergency_indicator = models.CharField(max_length=1, blank=True, null=True)
    channel_indicator = models.CharField(max_length=1, blank=True, null=True)
    number_of_pages = models.CharField(max_length=1, blank=True, null=True)
    schedule_period = models.CharField(max_length=1, blank=True, null=True)
    number_of_reserved_slots = models.CharField(max_length=1, blank=True, null=True)
    broadcast_message_type = models.CharField(max_length=1, blank=True, null=True)
    warning_period = models.CharField(max_length=1, blank=True, null=True)
    length_indicator = models.CharField(max_length=1, blank=True, null=True)
    keep_alive_repetition_period = models.CharField(max_length=1, blank=True, null=True)
    cause = models.IntegerField(blank=True, null=True)
    criticality_diagnostics = models.CharField(max_length=1, blank=True, null=True)
    warning_securityinfo = models.CharField(max_length=1, blank=True, null=True)
    broadcast_scheduled_area_list = models.CharField(max_length=1, blank=True, null=True)
    broadcast_cancelled_area_list = models.CharField(max_length=1, blank=True, null=True)
    broadcast_empty_area_list = models.CharField(max_length=1, blank=True, null=True)
    restarted_cell_list = models.IntegerField(blank=True, null=True)
    list_of_tais_restart = models.CharField(db_column='list_of_TAIs_restart', max_length=1, blank=True, null=True)  # Field name made lowercase.
    list_of_eais_restart = models.CharField(db_column='list_of_EAIs_restart', max_length=1, blank=True, null=True)  # Field name made lowercase.
    failed_cell_list = models.CharField(max_length=1, blank=True, null=True)
    failure_list = models.CharField(max_length=1, blank=True, null=True)
    number_of_broadcasts_completed_list = models.CharField(max_length=1, blank=True, null=True)
    radio_resource_loading_list = models.CharField(max_length=1, blank=True, null=True)
    recovery_indication = models.CharField(max_length=255, blank=True, null=True)
    service_areas_list = models.CharField(max_length=1, blank=True, null=True)
    typeoferror = models.CharField(max_length=1, blank=True, null=True)
    cell_list = models.CharField(max_length=1, blank=True, null=True)
    extras = models.CharField(max_length=1, blank=True, null=True)
    unknown_tracking_area_list = models.CharField(max_length=1, blank=True, null=True)
    messagetype_response = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Main'
        unique_together = (('timestamp', 'serial_number'),)


class NumberOfBroadcastsCompleted(models.Model):
    sn = models.IntegerField(db_column='SN', blank=True, null=True)  # Field name made lowercase.
    plmnidentity = models.TextField(db_column='PLMNidentity', blank=True, null=True)  # Field name made lowercase.
    lac = models.TextField(blank=True, null=True)
    sac = models.TextField(blank=True, null=True)
    number_broadcasts_completed = models.IntegerField(db_column='Number_Broadcasts_Completed', blank=True, null=True)  # Field name made lowercase.
    number_broadcasts_completed_info = models.CharField(db_column='Number_Broadcasts_Completed_Info', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Number_Of_Broadcasts_Completed'


class ServiceAreasList(models.Model):
    sn = models.IntegerField(db_column='SN', blank=True, null=True)  # Field name made lowercase.
    sn_response = models.IntegerField(db_column='SN_response', blank=True, null=True)  # Field name made lowercase.
    sn_indication = models.IntegerField(db_column='SN_indication', blank=True, null=True)  # Field name made lowercase.
    plmnidentity = models.TextField(db_column='PLMNidentity', blank=True, null=True)  # Field name made lowercase.
    sac = models.TextField(blank=True, null=True)
    lac = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Service_Areas_List'


class TaiCoordinates(models.Model):
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longtitude = models.CharField(max_length=255, blank=True, null=True)
    reference = models.IntegerField(blank=True, null=True)
    flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TAI_Coordinates'


class TaiList(models.Model):
    fk_ie31 = models.CharField(db_column='Fk_IE31', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fk_ie22 = models.CharField(db_column='FK_IE22', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fk_tai_broadcast_list = models.CharField(db_column='FK_TAI_broadcast_list', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fk_tai_cancelled_list = models.CharField(db_column='FK_TAI_cancelled_list', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fk_tracking_area_list_for_warning = models.CharField(db_column='FK_tracking_area_list_for_warning', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ecgi_list_fromtai = models.IntegerField(db_column='eCGI_list_fromTAI', blank=True, null=True)  # Field name made lowercase.
    plmnidentity = models.TextField(db_column='PLMNidentity', blank=True, null=True)  # Field name made lowercase.
    tac = models.TextField(db_column='TAC', blank=True, null=True)  # Field name made lowercase.
    fk_ie30 = models.CharField(db_column='FK_IE30', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAI_list'


class BroadcastCancelledAreaList(models.Model):
    idbroadcast_cancelled_area_list = models.IntegerField(blank=True, null=True)
    cell_id_cancelled_list = models.IntegerField(blank=True, null=True)
    tai_cancelled_list = models.IntegerField(db_column='TAI_cancelled_list', blank=True, null=True)  # Field name made lowercase.
    emergencyareaid_cancelled_list = models.IntegerField(db_column='EmergencyAreaID_cancelled_list', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'broadcast_cancelled_area_list'


class BroadcastScheduledAreaList(models.Model):
    idbroadcast_scheduled_area_list = models.IntegerField(blank=True, null=True)
    cell_id_broadcast_list = models.IntegerField(blank=True, null=True)
    tai_broadcast_list = models.IntegerField(db_column='TAI_broadcast_list', blank=True, null=True)  # Field name made lowercase.
    emergencyareaid_broadcast_list = models.IntegerField(db_column='EmergencyAreaID_broadcast_list', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'broadcast_scheduled_area_list'


class CriticalityDiagnostics(models.Model):
    idcriticality_diagnostics = models.CharField(max_length=1, blank=True, null=True)
    responseid_criticalitydiag = models.IntegerField(db_column='responseID_criticalityDiag', blank=True, null=True)  # Field name made lowercase.
    triggeringmessage = models.CharField(max_length=255, blank=True, null=True)
    procedurecriticality = models.CharField(max_length=255, blank=True, null=True)
    ie_criticalitydiagnostics = models.CharField(db_column='IE_criticalitydiagnostics', max_length=255, blank=True, null=True)  # Field name made lowercase.
    procedurecode = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'criticality_diagnostics'


class CriticalityDiagnostics3G(models.Model):
    sn = models.IntegerField(db_column='SN', blank=True, null=True)  # Field name made lowercase.
    error_indication = models.IntegerField(blank=True, null=True)
    procedurecode = models.IntegerField(db_column='ProcedureCode', blank=True, null=True)  # Field name made lowercase.
    triggeringmessage = models.CharField(db_column='TriggeringMessage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    procedurecriticality = models.CharField(db_column='ProcedureCriticality', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ie_id = models.IntegerField(db_column='IE_ID', blank=True, null=True)  # Field name made lowercase.
    ie_criticality = models.CharField(db_column='IE_Criticality', max_length=255, blank=True, null=True)  # Field name made lowercase.
    repitionnumber = models.IntegerField(db_column='RepitionNumber', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'criticality_diagnostics_3G'


class EcgiList(models.Model):
    fk_ie30 = models.CharField(db_column='FK_IE30', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fk_ie33 = models.CharField(db_column='FK_IE33', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fk_cell_id_broadcast_list = models.CharField(db_column='FK_cell_id_broadcast_list', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fk_cell_id_cancelled_list = models.CharField(db_column='FK_cell_id_cancelled_list', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fk_eaid_cancelled_list = models.CharField(db_column='FK_EAID_cancelled_list', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fk_ecgi_list_tai = models.IntegerField(db_column='FK_eCGI_list_TAI', blank=True, null=True)  # Field name made lowercase.
    fk_cell_id_list = models.CharField(db_column='FK_cell_id_list', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fk_ecgi_list_eai = models.IntegerField(db_column='FK_eCGI_list_EAI', blank=True, null=True)  # Field name made lowercase.
    plmnidentity = models.TextField(db_column='PLMNidentity', blank=True, null=True)  # Field name made lowercase.
    cell_id = models.CharField(max_length=255, blank=True, null=True)
    noofbroadcast = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eCGI_list'


class FailureList(models.Model):
    sn = models.IntegerField(db_column='SN', blank=True, null=True)  # Field name made lowercase.
    plmnidentity = models.TextField(db_column='PLMNidentity', blank=True, null=True)  # Field name made lowercase.
    lac = models.TextField(blank=True, null=True)
    sac = models.TextField(blank=True, null=True)
    cause = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'failure_list'


class ListofEcgi(models.Model):
    fk_tai_broadcast_list = models.IntegerField(db_column='FK_TAI_broadcast_list', blank=True, null=True)  # Field name made lowercase.
    fk_eaid_broadcast_list = models.IntegerField(db_column='FK_EAID_broadcast_list', blank=True, null=True)  # Field name made lowercase.
    fk_cell_id_cancelled_list = models.IntegerField(db_column='FK_cell_id_cancelled_list', blank=True, null=True)  # Field name made lowercase.
    fk_eaid_cancelled_list = models.IntegerField(db_column='FK_EAID_cancelled_list', blank=True, null=True)  # Field name made lowercase.
    ecgi_list = models.IntegerField(db_column='eCGI_list', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'listof_eCGI'


class RadioResourceLoadingList(models.Model):
    sn = models.IntegerField(db_column='SN', blank=True, null=True)  # Field name made lowercase.
    plmnidentity = models.TextField(db_column='PLMNidentity', blank=True, null=True)  # Field name made lowercase.
    lac = models.TextField(blank=True, null=True)
    sac = models.TextField(blank=True, null=True)
    availablebandwidth = models.IntegerField(db_column='AvailableBandwidth', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'radio_resource_loading_list'


class WarningAreaList(models.Model):
    idwarning_area_list = models.CharField(max_length=1, blank=True, null=True)
    cell_id_list = models.CharField(max_length=1, blank=True, null=True)
    tracking_area_list_for_warning = models.CharField(max_length=1, blank=True, null=True)
    emergency_area_id_list = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warning_area_list'
