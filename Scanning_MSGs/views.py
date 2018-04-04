# from __future__ import absolute_import

# from cbeinterf import *
# from .gsm7bit_codec import *

from django.http import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
import socket
from .forms import *
import pickle


HOST = 'localhost'#'192.168.1.183'  #
timeout = 1 # socket reading timeout
#
# msg = CBCCBEINTERFREQUEST()
# msg = msg[1]

PORT = 50007
# Create a socket connection.
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((HOST, PORT))

def Storing(ListOfEle):
    pass

@csrf_exempt
def AddMsg(request):
    handle = 0

    if request.method == 'POST':
        form = Message_IEs(request.POST)
        # format = form.s()
        if form.is_valid():
            # if form.s().is_valid():
            #     cd = form.cleaned_data
            #     print(cd)
            Msg_Ele = form.save(commit=False)
            Msg_Ele.save()

            return HttpResponseRedirect('/AllMessages/')


    else:
        form = Message_IEs()

    return render_to_response('addMsg.html', {'form':form}, RequestContext(request))


def AllMsgs(request):
    # print({'ParametersList': Main.objects.all()})
    # return render_to_response('AllMsg.html', {'ParametersList': Main.objects.all()})
    return render_to_response('maps.html')

