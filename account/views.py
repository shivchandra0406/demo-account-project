from copy import error
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from app.serializers import ProfessorSerializer
from .serializer import *
from .models import *
from .serializer import *
# Create your views here.
class Registrations(APIView):
    print("shivchnad")
    def post(self,request):
        try:
            data=request.data
            print(data)
            serializers=UserSerializer(data=data)
            if serializers.is_valid():
                serializers.save()
                return Response({
                    'status':"Success",
                    'data':serializers.data
                })
            return Response({
                'status':'Failure',
                'message':'somethin error',
                'data':serializers.errors
            })
        except Exception as e:
            print(e)
            return Response({
                'status':'Failure',
                'message':'somethin error'
            })
@api_view(['POST'])   
def otpVerify_view(request):
    try:
        data=request.data
        print(data)
        profile_obj=Profile.objects.get(user_id__username=data.get('username'))
        #serialiazer=ProfileSerializer(data=profile_obj)
        if profile_obj.otp==data.get('otp'):
            profile_obj.is_verfied=True
            serialiazer=ProfileSerializer(data=profile_obj)
            if serialiazer.is_valid():
               serialiazer.save()
               return Response({
                'data':serialiazer.data,
                    'message':'otp verified successfully'
                })
            return Response({
                'message':'your otp missmatch',
                'error':error

            })
        return Response({
            'message':'your user_id missmatch'
        })

    except Exception as e:
        print(e)
        return Response({
            'message':"somthing error",
            'error':error
        })