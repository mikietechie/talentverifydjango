import io

from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.request import Request
from rest_framework.utils.serializer_helpers import ReturnDict
from rest_framework import serializers
from rest_framework import permissions
from rest_framework import parsers
import pandas as pd

from app.models import Company, User, Department, Employee, Employment
from app.serializers import FileSerializer

@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
@parser_classes([parsers.FormParser, parsers.MultiPartParser])
def upload(request: Request):
    serialized = FileSerializer(data=request.data)
    status = 400
    if serialized.is_valid():
        file: InMemoryUploadedFile = serialized.validated_data["file"]
        extension = file.name.split(".")[-1]
        utype = serialized.validated_data["utype"]
        f = io.StringIO(file.read().decode("utf-8"))
        df: pd.DataFrame = None
        if extension == "csv":
            df = pd.read_csv(f)
        elif extension == "excel":
            df = pd.read_excel(f)
        elif extension == "json":
            df = pd.read_json(f)
        status = 200
    return Response(
        ReturnDict(
        {
            "file": df.to_string()
        },
        serializer=serializers.Serializer
        ),
        status
    )
