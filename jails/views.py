from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from collections import OrderedDict
import json
import ioc


def index(request):
    return render(request, 'jails/index.html')

def detail(request, jail_name):
    try:
        jail = ioc.Jail(jail_name)
    except (ioc.errors.JailNotFound):
        raise Http404('%s does not found' % jail_name)
    return render(request, 'jails/detail.html', {'jail': jail.config})

def new(request):
    try:
        distribution = ioc.Distribution()
    except(ioc.errors.IocageException):
        raise Http404('Jails does not found')
    return render(request, 'jails/new.html', {'distribution': distribution.releases})

def fetch_jails(request):
    try:
        jails = ioc.Jails()
        jails_json = []
        count = 1
        for jail in jails:
            jail.state.query()
            jail_dict = OrderedDict([
                ('id', count),
                ('jid', jail.jid),
                ('name', jail.name),
                ('status', 'up' if jail.running else 'down'),
                ('release', str(jail.release))
            ])
            jails_json.append(jail_dict)
            count += 1
        response = json.dumps(jails_json)
    except (ioc.errors.IocageException):
        return HttpResponse('API Error', status=500)
    return HttpResponse(response)

def fetch_releases(request):
    try:
        distribution = ioc.Distribution()
        releases_json = []
        for release in distribution.releases:
            release_dict = OrderedDict([
                ('name', release.name),
                ('fetched', ioc.Release(release.name).fetched)
            ])
            releases_json.append(release_dict)
        response = json.dumps(releases_json)
    except (ioc.errors.IocageException):
        return HttpResponse('API Error', status=500)
    return HttpResponse(response)

def release_download(request):
    try:
        response = json.loads(request.body)
        if response['release'] is None:
            return HttpResponse('release was none. Please selection release version', status=500)
        release = ioc.Release(response['release'])
        if release.fetched is True:
            return HttpResponse('%s was already downloaded. Skipping download.' % response['release'], status=409)
        release.fetch()
    except (ioc.errors.IocageException):
        return HttpResponse('API Error', status=500)
    return HttpResponse(response)

def start(request):
    try:
        response = json.loads(request.body)
        jail = ioc.Jail(response['jail_name'])
        jail.start()
    except (ioc.errors.JailAlreadyRunning):
        return HttpResponse('%s is already running' % response['jail_name'], status=409)
    except (ioc.errors.JailNotFound):
        raise Http404('%s does not found' % response['jail_name'])
    return HttpResponse('OK')

def stop(request):
    try:
        response = json.loads(request.body)
        jail = ioc.Jail(response['jail_name'])
        jail.stop()
    except (ioc.errors.JailNotRunning):
        return HttpResponse('%s is not running' % response['jail_name'], status=409)
    except (ioc.errors.JailNotFound):
        raise Http404('%s does not found' % response['jail_name'])
    return HttpResponse('OK')

def delete(request):
    try:
        response = json.loads(request.body)
        jail = ioc.Jail(response['jail_name'])
        jail.destroy()
    except (ioc.errors.JailNotFound):
        raise Http404('%s does not found' % response['jail_name'])
    return HttpResponse('OK')

def create(request):
    try:
        response = json.loads(request.body)
        release = ioc.Release(response['release'])
        jail = ioc.Jail(data=dict(name=response['jail_name']), new=True)
        jail.create(release)
    except(ioc.errors.JailAlreadyExists):
        return HttpResponse('%s is already exists' % response['jail_name'], status=409)
    return HttpResponse('OK')
