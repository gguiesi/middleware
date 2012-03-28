# Create your views here.
from django.http import HttpResponse
from suds.client import Client
import json

url = 'http://labimedsys.no-ip.org:8081/wssiam/ws/service?wsdl'

def index(request):
    client = Client(url)
    return HttpResponse(client)

def getEnv(request, user, password, version):
    client = Client(url)
    result = client.service.getEnv(user, password, version)
    return HttpResponse(json.dumps(json.loads(result), sort_keys=True, indent=4))

