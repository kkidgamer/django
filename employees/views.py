# employees/views.py
from rest_framework import generics
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer

# ==================== DEPARTMENT VIEWS ====================

# 1. Handles: Read All (GET) & Create (POST)
class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

# 2. ADD THIS FOR FULL CRUD: Handles Read One (GET), Update (PUT), and Delete (DELETE)
class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


# ==================== EMPLOYEE VIEWS ====================

# 1. Handles: Read All (GET) & Create (POST)
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# 2. ADD THIS FOR FULL CRUD: Handles Read One (GET), Update (PUT), and Delete (DELETE)
class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
