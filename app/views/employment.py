from app.models import Employment
from app.serializers import EmploymentSerializer
from app.views.base import BaseDetail, BaseList


class EmploymentList(BaseList):
    queryset = Employment.objects.all()
    serializer_class = EmploymentSerializer


class EmploymentDetail(BaseDetail):
    queryset = Employment.objects.all()
    serializer_class = EmploymentSerializer
