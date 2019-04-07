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
        bridge = libioc.BridgeInterface.BridgeInterface(name=response['bridge_name'], secure_vnet=True)
        jail = libioc.Jail(response['jail_name'])
        ipv4 = ipaddress.IPv4Interface(response['ipv4_addresses'])
        commands_created, commands_start = libioc.Network.Network(jail=jail, bridge=bridge, ipv4_addresses=[ipv4]).setup()
        jail.config["vnet"] = True
        jail.config["interfaces"] = f"{response['interfaces']}:{response['bridge_name']}"
        jail.config["ip4_addr"] = f"{response['interfaces']}|{response['ipv4_addresses']}"
        jail.save()
    except (ipaddress.AddressValueError):
        return JsonResponse({'reason': 'Address cannot be empty'}, status=400)
    except (libioc.errors.VnetBridgeDoesNotExist):
        return JsonResponse({'reason': '%s does not found' % response['bridge_name']}, status=400)
    except (libioc.errors.JailNotFound):
        return JsonResponse({'reason': '%s does not found' % response['jail_name']}, status=400)
    except (libioc.errors.IocException):
        return JsonResponse({'reason': 'API Error'}, status=500)
    return JsonResponse({'commands_created': commands_created, 'commands_start': commands_start}, status=200)


def get_jails(request):
    try:
        jails = libioc.Jails()
        jails_name_json = []
        for jail in jails:
            if jail.running:
                continue
            jail_dict = OrderedDict([
                ('name', jail.name)
            ])
            jails_name_json.append(jail_dict)
        response = json.dumps(jails_name_json)
    except (libioc.errors.IocException):
        return JsonResponse({'reason': 'API Error'}, status=500)
    return HttpResponse(response)
