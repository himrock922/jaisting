from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.http import JsonResponse
from collections import OrderedDict
from django.contrib.auth.decorators import login_required
import json
import libioc


@login_required
def index(request):
    return render(request, 'jails/index.html')


@login_required
def detail(request, jail_name):
    try:
        jail = libioc.Jail(jail_name)
    except (libioc.errors.JailNotFound):
        raise Http404('%s does not found' % jail_name)
    return render(request, 'jails/detail.html', {'jail': jail})


@login_required
def connect(request, jail_name):
    try:
        jail = libioc.Jail(jail_name)
    except (libioc.errors.JailNotFound):
        raise Http404('%s does not found' % jail_name)
    return render(request, 'jails/connect.html', {'jail': jail})


@login_required
def new(request):
    try:
        distribution = libioc.Distribution()
    except(libioc.errors.IocException):
        raise Http404('Jails does not found')
    return render(request, 'jails/new.html', {'distribution': distribution.releases})


def fetch_jails(request):
    try:
        jails = libioc.Jails()
        jails_json = []
        key_id = 1
        for jail in jails:
            jail_dict = OrderedDict([
                ('id', key_id),
                ('jid', jail.jid),
                ('name', jail.name),
                ('status', 'up' if jail.running else 'down'),
                ('release', str(jail.release))
            ])
            jails_json.append(jail_dict)
            key_id += 1
        response = json.dumps(jails_json)
    except (libioc.errors.IocException):
        return HttpResponse('API Error', status=500)
    return HttpResponse(response)


def fetch_releases(request):
    try:
        distribution = libioc.Distribution()
        releases_json = []
        for release in distribution.releases:
            release_dict = OrderedDict([
                ('name', release.name),
                ('fetched', libioc.Release(release.name).fetched)
            ])
            releases_json.append(release_dict)
        response = json.dumps(releases_json)
    except (libioc.errors.IocException):
        return HttpResponse('API Error', status=500)
    return HttpResponse(response)


def release_download(request):
    try:
        response = json.loads(request.body)
        if response['release'] is None:
            return HttpResponse('release was none. Please selection release version', status=500)
        release = libioc.Release(response['release'])
        if release.fetched is True:
            return HttpResponse('%s was already downloaded. Skipping download.' % response['release'], status=409)
        release.fetch()
    except FileNotFoundError:
        release.destroy()
        return HttpResponse('File Download Error', status=404)
    except (libioc.errors.IocException):
        release.destroy()
        return HttpResponse('API Error', status=500)
    return HttpResponse(response)


def start(request):
    try:
        response = json.loads(request.body)
        jail = libioc.Jail.Jail(response['jail_name'])
        jail.start()
    except (libioc.errors.JailAlreadyRunning):
        return HttpResponse('%s is already running' % response['jail_name'], status=409)
    except (libioc.errors.JailNotFound):
        raise Http404('%s does not found' % response['jail_name'])
    return HttpResponse('OK')


def stop(request):
    try:
        response = json.loads(request.body)
        jail = libioc.Jail.Jail(response['jail_name'])
        jail.stop()
    except (libioc.errors.JailNotRunning):
        return HttpResponse('%s is not running' % response['jail_name'], status=409)
    except (libioc.errors.JailNotFound):
        raise Http404('%s does not found' % response['jail_name'])
    return HttpResponse('OK')


def delete(request):
    try:
        response = json.loads(request.body)
        jail = libioc.Jail(response['jail_name'])
        jail.destroy()
    except (libioc.errors.JailNotFound):
        return JsonResponse({'reason': '%s does not found' % response['jail_name']}, status=404)
    return HttpResponse('OK')


def create(request):
    try:
        response = json.loads(request.body)
        release = libioc.Release(response['release'])
        jail = libioc.Jail(data=dict(name=response['jail_name']), new=True)
        jail.create(release)
    except(libioc.errors.JailAlreadyExists):
        return JsonResponse({'reason': '%s is already exists' % response['jail_name']}, status=409)
    return HttpResponse('OK')
