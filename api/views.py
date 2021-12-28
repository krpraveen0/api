#Importing the libraries
from django.shortcuts import render
from django.views.generic import View
import io
from rest_framework.parsers import JSONParser
from api.models import Students
from api.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


# Create your views here.
class StudentCRUDCBV(View):
    #Implementing the get method for an api
    def get(self,request,*args,**kwargs):
        #collecting the request body data in json_data variable

        json_data = request.body
        print(json_data)
        #converting the json_data into stream(encrypting with 1010)
        stream = io.BytesIO(json_data)
        #parsing the stream into the JSON structure data
        print(type(stream))
        data = JSONParser().parse(stream)
        print(data)
        id = data.get('id',None)
        if id is not None:
            students = Students.objects.get(id=id)
            #converting the students complex type from the db to python native type
            serializer = StudentSerializer(students)
            #rendering the python native type data as json type
            json_data = JSONRenderer().render(serializer.data)
            #sending the response json_data in the json structure
            return HttpResponse(json_data,content_type='application/json')
        qs = Students.objects.all()
        serializer = StudentSerializer(qs,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    #post request
    def post(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        serializer = StudentSerializer(stream)
        if serializer.is_valid():
            serializer.save()
            msg={'message':"Resource created Successfully"}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type="application/json")

    #updating the data
    def put(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id=data.get('id')
        student = Students.objects.get(id=id)
        serializer = StudentSerializer(s_no,data=student,partial=True)
        if serializer.is_valid():
            serializer.save()
            msg={'message':"Resource update Successfully.."}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
