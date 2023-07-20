from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status, serializers
from rest_framework.utils.serializer_helpers import ReturnDict

from app.models import User, Department, Company, Employee, Employment


@api_view(["GET"])
def admin(request: Request):
    ctx = {}
    ctx["counts"] = {
        "user": User.objects.count(),
        "department": Department.objects.count(),
        "company": Company.objects.count(),
        "employee": Employee.objects.count(),
        "employment": Employment.objects.count(),
    }
    return Response(
        ReturnDict(
            ctx,
            serializer = serializers.Serializer
        ),
        status.HTTP_200_OK
    )
