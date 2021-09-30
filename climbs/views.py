from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers
import json


def index(request):
    return HttpResponse("Hello, world. You're at the climbs index.")


def locations(request, location_id=None):
    if location_id is not None:
        data = model_to_dict(Locations.objects.get(id=location_id))
        return JsonResponse(data, safe=False, content_type="application/json")
    else:
        allLocations = Locations.objects.values_list('id')
        return JsonResponse({"all_location_data": list(allLocations)})

def getAreasForLocation(request, location_id):
    data = Areas.objects.filter(location__id=location_id).values()
    return JsonResponse({location_id+"-areas": list(data)})

def areas(request, location_id=None, area_id=None):
    if area_id is not None:
        data = model_to_dict(Areas.objects.get(id=area_id))
        return JsonResponse(data, safe=False, content_type="application/json")
    else:
        allAreas = Areas.objects.values_list('id')
        return JsonResponse({"all_area_data": list(allAreas)})

def getBouldersForArea(request, area_id, location_id=None):
    data = Boulders.objects.filter(area__id=area_id).values()
    return JsonResponse({area_id+"-boulders": list(data)})

def boulders(request, location_id=None, area_id=None, boulder_id=None):
    if boulder_id is not None:
        data = model_to_dict(Boulders.objects.get(id=boulder_id))
        return JsonResponse(data, safe=False, content_type="application/json")
    else:
        allBoulders = Boulders.objects.values_list('id')
        return JsonResponse({"all_boulder_data": list(allBoulders)})

def getClimbsForBoulder(request, boulder_id, area_id=None, location_id=None):
    data = Climbs.objects.filter(boulder__id=boulder_id).values()
    return JsonResponse({boulder_id+"-climbs": list(data)})

def climbs(request, boulder_id=None, area_id=None, location_id=None, climb_id=None):
    if climb_id is not None:
        data = model_to_dict(Climbs.objects.get(id=climb_id))
        return JsonResponse(data, safe=False, content_type="application/json")
    else:
        allClimbs = Locations.objects.values_list('id')
        return JsonResponse({"all_climb_data": list(allClimbs)})