from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Persons
from .serializers import PersonSerializer


class GenericPerson(generics.ListAPIView , generics.CreateAPIView):
    queryset = Persons.objects.all()
    serializer_class = PersonSerializer

class GenericPersonUpdate(generics.UpdateAPIView , generics.DestroyAPIView):
    queryset = Persons.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'id'



class ClassPerson(APIView):
    def get(self,request):
        person = Persons.objects.all()
        serializer = PersonSerializer(person,many = True)
        return Response(serializer.data)


    def post(self,request):
        return Response('This is post method in APIView')


@api_view(['GET','POST'])
def index(request):
    if request.method == 'GET':
        person_details = {
        'Name':'Radhika',
        'Age':32,
        'place':'Kottayam'
       }
        return Response(person_details)
    
    elif request.method == "POST":
        print("method is post")
        return Response('This is post method ')
    

@api_view(['GET','POST','PUT','PATCH',"DELETE"])
def person_view(request):
    if request.method == 'GET':
        person = Persons.objects.all()
        serializer = PersonSerializer(person,many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data
        obj = Persons.objects.get(id=data['id'])
        serializer = PersonSerializer(obj , data=data, partial = False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PATCH':
        data = request.data
        obj = Persons.objects.get(id=data['id'])
        serializer = PersonSerializer(obj , data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        data = request.data
        obj = Persons.objects.get(id=data['id'])
        obj.delete()
        return Response({'message':'Person deleted'})
    

class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Persons.objects.all()    


    
    
    


        