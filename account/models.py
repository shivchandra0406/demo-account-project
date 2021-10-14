from django.db import models
from django.contrib.auth.models import User
# Create your models here
class  Profile(models.Model):
    user_id=models.OneToOneField(User,on_delete=models.CASCADE)
    otp=models.CharField(max_length=20)
    is_verfied:models.BooleanField(default=False)

