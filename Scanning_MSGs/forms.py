__author__ = 'fissalalsharef'

from django import forms
from .models import *

from itertools import groupby, chain


# class MsgElements(forms.ModelForm):
#     END_Time = forms.CharField(max_length=70)
#     Start_Time = forms.CharField(max_length=70) #
#     List_Of_TAIs = forms.CharField(max_length=70)
#     Warning_Area_List = forms.CharField(max_length=70) #
#     Extend_Repitition_Period = forms.CharField(max_length=70)
#     Number_Of_Broadcast_Requested = forms.CharField(max_length=70) #
#     Warning_Type = forms.CharField(max_length=70)
#     OMC_ID = forms.CharField(max_length=70) #
#     Concurent_Warning_Indication = forms.CharField(max_length=70)
#     Send_Write_Replace_Warning_Indcation = forms.CharField(max_length=70) #
#     Gloabal_EnB_Id = forms.CharField(max_length=70) #
#     Repitition_Period = forms.IntegerField()
#     Data_Coding_Scheme = forms.IntegerField()
#     Service_Area_List = forms.CharField(max_length=70)
#     Catagory = forms.CharField(max_length=70)
#     Paging_ETWS_Indicator = forms.CharField(max_length=70)
#     Broadcast_Message_Validity_Indicator = forms.CharField(max_length=70)
#     Cell_List = forms.CharField(max_length=70)
#     Channel_Indicator = forms.CharField(max_length=70)
#     Emergancy_Indicator = forms.CharField(max_length=70)
#     Message_ID = forms.CharField(widget=forms.Select(choices=Type_of_msg), max_length = 70)
#     Message_Content = forms.CharField(max_length=100)

CHOICES=[('select1','select 1'),
         ('select2','select 2')]



class Message_IEs(forms.ModelForm):
    # broadcast_message_content = forms.CharField(max_length=70)
    # message_identifier = forms.CharField(max_length=70)
    # category = forms.CharField(max_length=70)
    # list_of_tais = forms.CharField(max_length=70)
    # warning_area_list = forms.CharField(max_length=70)
    # repetition_period = forms.CharField(max_length=70)
    # extended_repetition_period = forms.CharField(max_length=70)
    # number_of_broadcasts_requested = forms.CharField(max_length=70)
    # messagetype = forms.CharField(max_length=70)
    # warning_security_information = forms.CharField(max_length=70)
    # data_coding_scheme = forms.CharField(max_length=70)
    # warning_message_content = forms.CharField(max_length=70)
    # omc_id = forms.CharField(max_length=70)
    # concurrent_warning_message_indicator = forms.CharField(max_length=70)
    # send_write_replace_warning_indication = forms.CharField(max_length=70)
    # global_enb_id = forms.CharField(max_length=70)
    # send_stop_warning_indication = forms.CharField(max_length=70)
    # stop_all_indicator = forms.CharField(max_length=70)
    # paging_etws_indicator = forms.CharField(max_length=70)
    # message_structure = forms.CharField(max_length=70)
    # warning_type = forms.CharField(max_length=70)
    # broadcast_message_content_validity_indicator = forms.CharField(max_length=70)
    # emergency_indicator = forms.CharField(max_length=70)
    # channel_indicator = forms.CharField(max_length=70)
    # number_of_pages = forms.CharField(max_length=70)
    # schedule_period = forms.CharField(max_length=70)
    # number_of_reserved_slots = forms.CharField(max_length=70)
    # broadcast_message_type = forms.CharField(max_length=70)
    # warning_period = forms.CharField(max_length=70)
    # length_indicator = forms.CharField(max_length=70)
    # keep_alive_repetition_period = forms.CharField(max_length=70)
    # cause = forms.CharField(max_length=70)
    # criticality_diagnostics = forms.CharField(max_length=70)
    # warning_securityinfo = forms.CharField(max_length=70)
    # broadcast_scheduled_area_list = forms.CharField(max_length=70)
    # broadcast_cancelled_area_list = forms.CharField(max_length=70)
    # broadcast_empty_area_list= forms.CharField(max_length=70)
    # restarted_cell_list = forms.CharField(max_length=70)
    # list_of_tais_restart = forms.CharField(max_length=70)
    # list_of_eais_restart = forms.CharField(max_length=70)
    # failed_cell_list = forms.CharField(max_length=70)
    # failure_list = forms.CharField(max_length=70)
    # number_of_broadcasts_completed_list = forms.CharField(max_length=70)
    # radio_resource_loading_list = forms.CharField(max_length=70)
    # recovery_indication = forms.CharField(max_length=70)
    # service_areas_list = forms.CharField(max_length=70)
    # typeoferror = forms.CharField(max_length=70)
    # cell_list = forms.CharField(max_length=70)
    # extras = forms.CharField(max_length=70)
    # unknown_tracking_area_list = forms.CharField(max_length=70)


    class Meta:
        model = Main
        fields ='__all__'

    # class s(forms.Form):
    #     like = forms.ChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple())



