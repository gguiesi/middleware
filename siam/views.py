# Create your views here.
from django.http import HttpResponse
from suds.client import Client
import json

url = 'http://labimedsys.no-ip.org:8081/wssiam/ws/service?wsdl'
client = Client(url)

def index(request):
    return HttpResponse(client)

def getEnv(request, user, password, version):
    result = client.service.getEnv(user, password, version)
    return HttpResponse(json.dumps(json.loads(result), sort_keys=True, indent=4))

def authUser(request, user, password, version):
    result = client.service.authUser(user, password, version)
    return HttpResponse(json.dumps(json.loads(result), sort_keys=True, indent=4))

def contactUs(request):
    result = client.service.contactUs()
    return HttpResponse(json.dumps(json.loads(result), sort_keys=True, indent=4))

def executeAction(request, user, password, version, idAction ,idDev, param, idEnv):
    result = client.service.executeAction(user, password, version, idAction, idDev, param, idEnv)
    return HttpResponse(json.dumps(json.loads(result), sort_keys=True, indent=4))

def getDevByEnv(request, user, password, version, idEnv, idDev):
    result = client.service.getDevByEnv(user, password, version, idEnv, idDev)
    return HttpResponse(json.dumps(json.loads(result), sort_keys=True, indent=4))

def getMonitorByDev(request, user, password, version, date, idDev):
    result = client.service.getMonitorByDev(user, password, version, date, idDev)
    return HttpResponse(json.dumps(json.loads(result), sort_keys=True, indent=4))

def getReportByDev(request, user, password, version, date, idDev):
    result = client.service.getReportByDev(user, password, version, date, idDev)
    return HttpResponse(json.dumps(json.loads(result), sort_keys=True, indent=4))

def getReport(request, user, password, version, date, idEnv, idDev, idUser):
    result = client.service.getReport(user, password, version, date, idEnv, idDev, idUser)
    return HttpResponse(json.dumps(json.loads(result), sort_keys=True, indent=4))

def getProfile(request, user, password, version):
    result = client.service.getProfile(user, password, version)
    return HttpResponse(json.dumps(json.loads(result), sort_keys=True, indent=4))

def panicActive(request, user, password, version):
    result = client.service.panicActive(user, password, version)
    return HttpResponse(json.dumps(json.loads(result), sort_keys=True, indent=4))

def panicInfo(request, user, password, version):
    result = client.service.panicInfo(user, password, version)
    return HttpResponse(json.dumps(json.loads(result), sort_keys=True, indent=4))

def setDevice(request, user, password, version, device):
    result = client.service.setDevice(user, password, version, device)
    return HttpResponse(json.dumps(json.loads(result), sort_keys=True, indent=4))

def setProfileActive(request, user, password, version, device):
    result = client.service.setProfileActive(user, password, version, device)
    return HttpResponse(json.dumps(json.loads(result), sort_keys=True, indent=4))

def getStatusByDev(request, user, password, version, idEnv, idDev):
    result = client.service.getStatusByDev(user, password, version, idEnv, idDev)
    return HttpResponse(json.dumps(json.loads(result), sort_keys=True, indent=4))

def getMessageReport(request, user, password, version):
    result = client.service.getMessageReport(user, password, version)
    return HttpResponse(json.dumps(json.loads(result), sort_keys=True, indent=4))

def getPassKey(request, user, password, version):
    result = client.service.getPassKey(user, password, version)
    return HttpResponse(json.dumps(json.loads(result), sort_keys=True, indent=4))

def getTpDev(request, user, password, version, idTpDev):
    result = client.service.getPassKey(user, password, version)
    return HttpResponse(json.dumps(json.loads(result), sort_keys=True, indent=4))

def newPassword(request, user):
    result = client.service.newPassword(user)
    return HttpResponse(json.dumps(json.loads(result), sort_keys=True, indent=4))

def sendPassword(request, sendPassword):
    result = client.service.sendPassword(sendPassword)
    return HttpResponse(json.dumps(json.loads(result), sort_keys=True, indent=4))
