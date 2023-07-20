from app.models import Company
from app.serializers import CompanySerializer
from app.views.base import BaseDetail, BaseList


class CompanyList(BaseList):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDetail(BaseDetail):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
