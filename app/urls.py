from django.urls import path
from .views import Student1, StudentView,getProfessor_view,getSubject
from rest_framework.routers import DefaultRouter
# stu=DefaultRouter()
# stu.register('student1',Student1,basename='student1')
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'student1', Student1, basename='student1')



urlpatterns = [
   path('getsubject/',getSubject),
   path('getProfessor/',getProfessor_view),
   path('student/',StudentView.as_view()),
   
]
urlpatterns += router.urls
