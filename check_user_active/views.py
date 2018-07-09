from register.models import Register
from rest_framework import generics
# from ticket.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions
from django.shortcuts import get_object_or_404
from django.db.models import Count 
from django.http import JsonResponse

# class Get_listList(generics.ListCreateAPIView):
#  queryset = Ticket.objects.all()
#  serializer_class = Get_listSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class StatusCode(object):
    OK = 200
    NOT_FOUND = 404
    # add more status code according to your need
import json
from django.http import HttpResponse
 
def JSONResponse(data = None, status = StatusCode.OK):
    if data is None:
        return HttpResponse(status)
    if data and type(data) is dict:
        return HttpResponse(json.dumps(data, indent = 4, encoding = 'utf-8', sort_keys = True), \
            mimetype = 'application/json', status = status)
    else:
        return HttpResponse(status = StatusCode.NOT_FOUND)



def get_queryset(request):
  username = request.META.get('HTTP_USERNAME')
  level = request.META.get('HTTP_LEVEL')

  fields = []

  if(Register.objects.filter(username=username,level=level,is_active="1")):
  	fields.append(
          {
           'status':200
          }
        )
  else:
  	fields.append(
          {
           'status':400
          }
        )

  import sys
  print (sys.stderr, fields)
  
  
  
    
  return JsonResponse((list(fields)),safe=False)
  

