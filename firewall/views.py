from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
from collections import OrderedDict
from django.http import Http404
from django.contrib.auth.decorators import login_required
import json
import libioc
from libipfw.ipfw_list import IPFW_List


@login_required
def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'firewall/index.html')



def fetch_all_lists(request: HttpRequest) -> JsonResponse:
    firewall = IPFW_List()
    response = firewall.all_results()
    return JsonResponse(dict(firewall_lists=response))
