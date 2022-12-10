from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from app.api.serializers import UserSerializers
from app.models.User_Models import User 

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    
    serializer_class = UserSerializers
    queryset = User.objects.all()
    