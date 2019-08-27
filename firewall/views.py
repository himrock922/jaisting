from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
from collections import OrderedDict
from django.http import Http404
from django.contrib.auth.decorators import login_required
import json
import libioc
from libipfw import command_exec


@login_required
def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'firewall/index.html')


def fetch_all_lists(request: HttpRequest) -> JsonResponse:
    firewall = command_exec.IPFW()
    response = firewall.results()
    return JsonResponse(dict(firewall_lists=response))

def add(request: HttpRequest) -> JsonResponse:
    try:
        command: str = ""
        response = json.loads(request.body)
        command = ' '.join([line for line in response.values()])
        firewall = command_exec.IPFW()
        firewall.add(command)
    except (command_exec.errors.AddExecError):
        return HttpResponse('API Error', status=500)
    return HttpResponse('OK')

def delete(request: HttpRequest) -> JsonResponse:
    try:
        command: str = ""
        response = json.loads(request.body)
        command = ' '.join([line for line in response.values()])
        firewall = command_exec.IPFW()
        firewall.delete(command)
    except (command_exec.errors.AddExecError):
        return HttpResponse('API Error', status=500)
    return HttpResponse('OK')