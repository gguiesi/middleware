# Create your views here.
from django.http import HttpResponse
from suds.client import Client
import json

def index(request):
    url = 'http://labimedsys.no-ip.org:8081/wssiam/ws/service?wsdl'
    client = Client(url)
    result = client.service.getEnv('siam', 'siam1234', '101')
    return HttpResponse(json.dumps(json.loads(result), sort_keys=True, indent=4))
