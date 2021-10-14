from copy import error
from django.core.checks import messages
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StudenSerializer, SubjectSerializer,ProfessorSerializer
from .models import Student, Subject,Professor
from rest_framework import serializers, status
from rest_framework.decorators import action
#import urls
# Create your views here.
class Student1(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudenSerializer
    def list(self, request):
        objs = Student.objects.all()
        if request.GET.get('id'):
            objs = objs.exclude(pid = request.GET.get('id'))
        serializer = StudenSerializer(objs , many= True)
        return Response({
            'status' : 200,
            'message' : 'data',
            'data' : serializer.data
        })
    
    @action(methods=['GET'], detail=False)
    def getprofessor(self,request,pk=None):
        data=Professor.objects.all()
        serializer=ProfessorSerializer(data,many=True)
        return Response({
                'message':"data get successfully",
                'data':serializer.data
            })
        



@api_view(['GET'])
def getProfessor_view(request):
    try:
        print('demo')
        data=Professor.objects.all()
        a=ProfessorSerializer(data,many=True)
        print(a)
        return Response(
            {'status':200,'details':a.data,"message":"All data find successfuly"}
        )
    except Exception as e:
        print(e)
        return Response(
            {'status':401,"message":a.error_messages}

        )
    
@api_view(['GET'])
def getSubject(request):
    try:
        print("shivchand")
        subject=Subject.objects.all()
        data=SubjectSerializer(subject,many=True)
        print(data)
        
        return Response({
                'status':201,
                "message":data.data
            })
     
    except Exception as e:
        print(e)
        return Response(
            {'status':401,"message":data.error_messages}

        )
class StudentView(APIView):
    
    def get(self,request):
        try:
            id=request.GET.get('pid')
            #id=request.GET.get('id')
            print(".........................................",id)
            if id is not None:
                data=Student.objects.filter(pid=id)
                
                print(".......................................................",data)
                if data:
                    serializers=StudenSerializer(data,many=True)
                    return Response(serializers.data,status=status.HTTP_200_OK)
                else:
                    return Response({'message':'Id not found'})
                #print(request.query_params)
                
                #print("hiiiii...................",id)
            else:
                data=Student.objects.all()
                print(data)
                serializers=StudenSerializer(data,many=True)
                return Response(serializers.data,status=status.HTTP_200_OK)
                
        except Exception as Ex:
            print(Ex)
            return Response({
                'status':status.HTTP_404_NOT_FOUND,
                'message':"id is not found"
            })
                
    def post(self,request):
        try:
            data=request.data
            serializer=StudenSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                # return Response({
                #     'status':200,
                #     'data':serializer.data,
                #     'message':'Data send'
                # })
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response({
                    'status':400,
                    'error':serializer.errors,
                    'message':'Invalid data'
                })
        except Exception as e:
            return Response({
                    'status':404,
                    'message':serializer.errors,
                    
                })

    def patch(self,request):
        try:
            #print("----------------------------",request.data)
            id=request.data['pid']
           # print("-----------_________________",id)
            data=Student.objects.get(pid=id)
            # if data:
            serializer=StudenSerializer(data,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'message':"data updated successfully",
                    'data':serializer.data
                    })
        except Exception as e:
            return Response({
                        'message':"Error comming",
                        'Error':e
                    })
    
    def delete(self,request):
        try:
            id=request.GET.get('id')
            data=Student.objects.filter(pid=id).delete()
            #Serializer=StudenSerializer(data)
            return Response({
                'messages':'deleted successfully',
                'data':data
            })
        except Exception as e:
            print(e)
            return Response({
                'message':'error in removing',
                'Error':e
                
            })

