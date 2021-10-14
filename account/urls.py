from django.urls import path
from .views import *
urlpatterns = [
    path('registration/',Registrations.as_view()),
    path('verifyotp/',otpVerify_view),
   
]