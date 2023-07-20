from rest_framework import serializers

from .models import User, Department, Company, Employee, Employment


# class UserMiniSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("id", "username", "email", "first_name", "last_name")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}


class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "role", "all_permissions", "initials_picture_url", "__str__", "is_superuser", "is_staff")
        extra_kwargs = {'password': {'write_only': True}}
        


# class DepartmentMiniSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Department
#         fields = ("id", "name")


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


# class CompanyMiniSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Company
#         fields = ("id", "name", "registration_number", "contact_person", "number_of_employees")


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("id", 
            "name",
            "date_of_registration",
            "registration_number",
            "address",
            "departments",
            "contact_person",
            "contact_phone",
            "email_address",
            "department_names",
            "number_of_employees"
        )


# class EmployeeMiniSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = ("id", "name", "id_number", "contact_phone", "email_address", "trade")


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


# class EmploymentMiniSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employment
#         fields = ("id", "role", "date_started", "date_left", "data")


class EmploymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employment
        fields = (
            "id",
            "department",
            "employee",
            "company",
            "role",
            "date_started",
            "date_left",
            "duties",
        )


class FileSerializer(serializers.Serializer):
    file = serializers.FileField()
    utype = serializers.CharField()
