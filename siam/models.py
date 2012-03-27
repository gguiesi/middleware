from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    
class Consults(models.Model):
    service = models.ForeignKey(Service)
    name = models.CharField(max_length=200)
    parameters = models.CharField(max_length=200)
    result = models.CharField(max_length=200)
    consult_date = models.DateTimeField('date consulted')