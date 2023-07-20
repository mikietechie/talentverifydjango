from app.models import Department
from app.serializers import DepartmentSerializer
from app.views.base import BaseDetail, BaseList


class DepartmentList(BaseList):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetail(BaseDetail):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


