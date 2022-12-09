from rest_framework import serializers
from app.models.User_Models import User

class UserSerializers(serializers.ModelSerializer):
    
    class Meta():       
        model = User
        fields = '__all__'      