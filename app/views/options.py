from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.utils.serializer_helpers import ReturnDict
from rest_framework import serializers

from app.models import Company, User, Department, Employee, Employment

@api_view(["GET"])
def company_form(request: Request):
    pk = request.GET.get("id")
    instance = Company.objects.get(id=int(pk)) if pk else Company()
    return Response(
        ReturnDict(
        instance.get_form_options(),
        serializer=serializers.Serializer
        ),
        200
    )

@api_view(["GET"])
def employment_form(request: Request):
    pk = request.GET.get("id")
    instance = Employment.objects.get(id=int(pk)) if pk else Employment()
    return Response(
        ReturnDict(
        instance.get_form_options(),
        serializer=serializers.Serializer
        ),
        200
    )
