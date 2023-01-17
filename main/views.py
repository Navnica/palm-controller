from django.shortcuts import render, HttpResponseRedirect
from controller_api.controller import OSController


def index(request):
    return render(request, 'main/index.html', {'processes': OSController.get_all_processes()})


def process_kill(request, pid):
    OSController.kill_process(pid)
    return HttpResponseRedirect('/')