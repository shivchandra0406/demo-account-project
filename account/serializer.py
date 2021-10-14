#
# from typing_extensions import Required
from django.contrib.auth.models import User
from django.db.models import fields
from .models import *
import random
from  .mail import *
from rest_framework import serializers
class UserSerializer(serializers.ModelSerializer):
    first_name=serializers.CharField(required=True)
    last_name=serializers.CharField(required=True)
    email=serializers.EmailField(required=True)
    class Meta:
        model=User
        fields=['username','password','first_name','last_name','email']
    def create(self, validated_data):
        first_name=validated_data['first_name']
        last_name=validated_data['last_name']
        email=validated_data['email']
        username=validated_data['username']
        password=validated_data['password']
        obj=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username
        
        )
        obj.set_password(password)
        obj.save()
        otp=random.randint(10000,99999)
        activate_url = f'{otp}'
        Profile.objects.create(
            user_id=obj,
            otp=otp
        )
    
        send_otp(obj.email,obj.first_name,activate_url)
        return obj

class ProfileSerializer(serializers.ModelSerializer):
    users=serializers.SerializerMethodField()
    class Meta:
        model=Profile
        fields='__all__'
        dept=1
    def get_users(self,obj):
        serializer =UserSerializer(obj.users.all(),many=True)
        return serializer.data