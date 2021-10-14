from rest_framework import serializers
from rest_framework.views import exception_handler
from .models import *


# class Student(serializers.Serializer):
#     mobile_no=serializers.CharField()
#     rool_no=serializers.IntegerField()



class SubjectSerializer(serializers.ModelSerializer):
    
    #subject = ProfessorSerializer(many=True,read_only=True)
    class Meta:
       model=Subject
       exclude = ['created_at' , 'updated_at']
        
class ProfessorSerializer(serializers.ModelSerializer):
    subjects=serializers.SerializerMethodField()
    class Meta:
        model = Professor
        exclude = ['created_at' , 'updated_at']
        depth = 1
    def get_subjects(self,obj):
        #print(obj)
        serializer =SubjectSerializer(obj.subjects.all(),many=True)
        return serializer.data
   
class StudenSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        exclude = ['created_at' , 'updated_at']
    # def has_number(self,text):
    #      return any(t.isdigit() for t in text)
    # def validate(self,validatedata):
    #     print
    #     if 'roll_no' in validatedata:
    #         if self.has_number(validatedata['roll_no']):
    #             raise serializers.ValidationError("rollno connot be number")
    #     return validatedata
         