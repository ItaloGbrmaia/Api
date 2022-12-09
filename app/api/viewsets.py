from rest_framework import viewsets
from app.api.serializers import UserSerializers
from app.models import User 

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()
    