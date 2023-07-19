from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated

from app.serializers import UserAuthSerializer

class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, *args, **kwargs):
        serialized_user = UserAuthSerializer(instance=request.user)
        return Response(
            serialized_user.data,
            status=status.HTTP_200_OK
        )
