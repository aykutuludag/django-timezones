from django.shortcuts import render
from django.http import JsonResponse
import json
import os

# Create your views here.

def home(request):
    return render(request, 'map/index.html')

def timezone_geojson(request):
    file_path = os.path.join('static', 'timezones.geojson')
    with open(file_path, encoding='utf-8') as f:
        data = json.load(f)
        return JsonResponse(data)