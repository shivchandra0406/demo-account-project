from django.db import models

# Create your models here.
#from typing import AbstractSet
from django.db import models
import uuid

#from django.db.models.fields import DateField, DateTimeField
# Create your models here.
class BaseModel(models.Model):
    pid=models.UUIDField(default=uuid.uuid4 , primary_key=True , editable=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Student(BaseModel):
    gender_choices=(('male','male'),('female','female'))
    name=models.CharField(max_length=25)
    roll_no=models.CharField(max_length=10)
    mobile_no=models.CharField(max_length=12)
    gender=models.CharField(max_length=6,choices=gender_choices)

class Subject(BaseModel):
    subName=models.CharField(max_length=20)
    
    def __str__(self):
        return self.subName
class Professor(BaseModel):
    p_fname=models.CharField(max_length=20)
    p_lname=models.CharField(max_length=20)
    subjects=models.ManyToManyField(Subject,blank=True,null=True)
    def __str__(self):
        return self.p_fname






