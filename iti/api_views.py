from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView,CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.utils import serializer_helpers
from .serializer import StudentSerializer
from .models import Student


class StudentList (ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    def get_queryset(self):
        queryset = Student.objects.all()
        return queryset

class  StudentCreate(CreateAPIView):
    serializer_class=StudentSerializer

    def create(self,request,*args,**kwargs):
        print(request.POST)
        return super().create(request,*args, **kwargs)