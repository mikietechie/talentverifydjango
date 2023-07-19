from app.models import Employee
from app.serializers import EmployeeSerializer
from app.views.base import BaseDetail, BaseList


class EmployeeList(BaseList):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetail(BaseDetail):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
