import json
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse(json.dumps({'file_id': 200232, 'filename': 'sasasas' , 'links_to' : 'somelink.com'}))
    # return HttpResponse("Hello, world. You're at the polls index.")