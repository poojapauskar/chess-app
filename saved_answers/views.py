from saved_answers.models import Saved_answers
from register.models import Register
from saved_answers.serializers import Saved_answersSerializer
from rest_framework import generics
# from register.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions

class Saved_answersList(generics.ListAPIView):
 queryset = Saved_answers.objects.all()
 serializer_class = Saved_answersSerializer

class Saved_answersDetail(generics.RetrieveUpdateDestroyAPIView):
 queryset = Saved_answers.objects.all()
 serializer_class = Saved_answersSerializer
 # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
 #                      IsOwnerOrReadOnly,)




class Update_details(generics.ListCreateAPIView):
 def put(self, request, *args, **kwargs):
  from django.http import JsonResponse

  
  import sys
  username= request.data['username']
  level= request.data['level']
  seconds= request.data['seconds']
  answer1= request.data['a1']
  answer2= request.data['a2']
  answer3= request.data['a3']
  answer4= request.data['a4']
  answer5= request.data['a5']
  answer6= request.data['a6']
  answer7= request.data['a7']
  answer8= request.data['a8']
  answer9= request.data['a9']
  answer10= request.data['a10']
  answer11= request.data['a11']
  answer12= request.data['a12']
  answer13= request.data['a13']
  answer14= request.data['a14']
  answer15= request.data['a15']
  answer16= request.data['a16']
  answer17= request.data['a17']
  answer18= request.data['a18']
  answer19= request.data['a19']
  answer20= request.data['a20']
  
 

  details=[]
  if(Register.objects.filter(username=username,level=level,is_active=0).exists()):
    details.append(
                  {
                   'status':400,
                   'message':'Session expired',
                   # 'result':list(update),
                  }
                 )
    from django.http import JsonResponse
    return JsonResponse(details[0],safe=False)

  else:
    if(Saved_answers.objects.filter(username=username,level=level).exists()):
      objects=Saved_answers.objects.filter(username=username,level=level).update(seconds=seconds,answer1=answer1,answer2=answer2,answer3=answer3,answer4=answer4,answer5=answer5,answer6=answer6,answer7=answer7,answer8=answer8,answer9=answer9,answer10=answer10,answer11=answer11,answer12=answer12,answer13=answer13,answer14=answer14,answer15=answer15,answer16=answer16,answer17=answer17,answer18=answer18,answer19=answer19,answer20=answer20)
      details.append(
                  {
                   'status':200,
                   'message':'Data saved',
                   # 'result':list(update),
                  }
                 )
    else:
      objects=Saved_answers.objects.create(seconds=seconds,username=username,level=level,answer1=answer1,answer2=answer2,answer3=answer3,answer4=answer4,answer5=answer5,answer6=answer6,answer7=answer7,answer8=answer8,answer9=answer9,answer10=answer10,answer11=answer11,answer12=answer12,answer13=answer13,answer14=answer14,answer15=answer15,answer16=answer16,answer17=answer17,answer18=answer18,answer19=answer19,answer20=answer20)
      details.append(
                  {
                   'status':200,
                   'message':'Data saved',
                   # 'result':list(update),
                  }
                 )
    from django.http import JsonResponse
    return JsonResponse(details[0],safe=False)

