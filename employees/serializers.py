# employees/serializers.py

from rest_framework import serializers
from .models import Employee, Department


# ==============================
# DEPARTMENT SERIALIZER
# ==============================
class DepartmentSerializer(serializers.ModelSerializer):
    """
    This serializer converts Department model data
    into JSON format and also allows JSON data
    to be converted back into Django objects.

    In simple terms:
    👉 It acts as a bridge between Django models and API responses.
    """

    class Meta:
        model = Department
        fields = '__all__'
        # This means:
        # Include ALL fields from the Department model (e.g. id, name)


# ==============================
# EMPLOYEE SERIALIZER
# ==============================
class EmployeeSerializer(serializers.ModelSerializer):
    """
    This serializer handles Employee data for API.

    IMPORTANT CONCEPT:
    ------------------
    We are using "nested serializer" here.

    That means:
    👉 Instead of returning only department ID,
       we return full Department details inside Employee JSON.

    Example OUTPUT:
    {
        "id": 1,
        "first_name": "John",
        "department": {
            "id": 2,
            "name": "IT"
        }
    }

    This is very useful when frontend needs readable data
    instead of just foreign key IDs.
    """

    # NESTED RELATIONSHIP
    # This replaces department ID with full department object
    department = DepartmentSerializer(read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'
        # Includes:
        # - first_name
        # - last_name
        # - email
        # - salary
        # - role
        # - department (now expanded as object)
        # - timestamps (date_joined, last_updated)