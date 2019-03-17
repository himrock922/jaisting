from django.shortcuts import render
from django.http import HttpResponse
from collections import OrderedDict
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
import libioc
import ipaddress

@login_required
def new(request):
    return render(request, 'networks/new.html')

def create(request):
    try:
        response = json.loads(request.body)
        print(response['bridge_name'])
        print(response['ipv4_addresses'])
        bridge = libioc.BridgeInterface.BridgeInterface(name=response['bridge_name'], secure_vnet=True)
        jail = libioc.Jail(response['jail_name'])
        ipv4 = ipaddress.IPv4Interface(response['ipv4_addresses'])
        commands_created, commands_start = libioc.Network.Network(jail=jail, bridge=bridge, ipv4_addresses= [ipv4]).setup()
    except (ipaddress.AddressValueError):
        return JsonResponse({'reason': 'Address cannot be empty'}, status=400)
    except (libioc.errors.VnetBridgeDoesNotExist):
        return JsonResponse({'reason': '%s does not found' % response['bridge_name']}, status=400)
    except (libioc.errors.JailNotFound):
        return JsonResponse({'reason': '%s does not found' % response['jail_name']}, status=400)
    except (libioc.errors.IocException):
        return JsonResponse({'reason': 'API Error'}, status=500)
    return JsonResponse({'commands_created': commands_created, 'commands_start': commands_start}, status = 200)

def get_jails(request):
    try:
        jails = libioc.Jails()
        jails_name_json = []
        count = 1
        for jail in jails:
            jail_dict = OrderedDict([
                ('name', jail.name)
            ])
            jails_name_json.append(jail_dict)
            count += 1
        response = json.dumps(jails_name_json)
    except (libioc.errors.IocException):
        return JsonResponse({'reason': 'API Error'}, status=500)
    return HttpResponse(response)