from django.shortcuts import render
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
from django.http import JsonResponse
from datetime import datetime
import pytz

# Create your views here.


#@api_view(['GET'])
def info_view(request):
    current_time = datetime.now(pytz.UTC).strftime('%Y-%m-%dT%H:%M:%SZ')

    data = {
        'email': 'torohkiss@gmail.com',
        'current_datetime': current_time,
        'github_url': "https://github.com/torohkiss/hng",
    }

    return JsonResponse(data, json_dumps_params={'indent': 2})
