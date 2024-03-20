from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True, methods=['GET'])
    def employees(self, request, pk=None):
        company = Company.objects.get(pk=pk)
        employees = Employee.objects.filter(company=company)
        emp_serializer = EmployeeSerializer(employees, many=True, context={'request': request})
        return Response(emp_serializer.data)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

