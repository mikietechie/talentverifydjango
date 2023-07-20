from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.utils.serializer_helpers import ReturnDict
from rest_framework import serializers

from app.serializers import UserAuthSerializer
from app.models import User

class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, *args, **kwargs):
        serialized_user = UserAuthSerializer(instance=request.user)
        return Response(
            serialized_user.data,
            status=status.HTTP_200_OK
        )
    
    def post(self, request: Request, *args, **kwargs):
        ctx = {}
        status = 400
        u: User  =request.user
        data = request.data
        print(data)
        if u.check_password(data["current_password"]):
            u.password = data["new_password"]
            u.first_name = data["first_name"]
            u.last_name = data["last_name"]
            u.username = data["username"]
            u.email = data["email"]
            u.save()
            status = 200
        else:
            ctx["Passwords"] = ["Passwords did not match"]
        return Response(
            ReturnDict(
                ctx,
                serializer = serializers.Serializer
            ),
            status=status
        )
