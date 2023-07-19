from app.models import User
from app.serializers import UserSerializer
from app.views.base import BaseDetail, BaseList


class UserList(BaseList):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(BaseDetail):
    queryset = User.objects.all()
    serializer_class = UserSerializer
