from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import EmployeesSerializer
from .models import Employees

class EmployeeDetails(APIView):
    def get_object(self, id):
        return Employees.objects.get(id=id)

    def get(self, request, id=None):
        if id:
            employee = self.get_object(id)
            serializer = EmployeesSerializer(employee)
        else:
            employees = Employees.objects.all()
            serializer = EmployeesSerializer(employees, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request, id):
        employee = Employees.objects.get(id=id)
        serializer = EmployeesSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request, id):
        employee = Employees.objects.get(id=id)
        serializer = EmployeesSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id):
        employee = Employees.objects.get(id=id)
        employee.delete()
        return Response('Name deleted successfully')