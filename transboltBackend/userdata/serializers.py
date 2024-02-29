from rest_framework import serializers
from .models import UserData , VehicleModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'
def create(self , validated_data):
    return UserData.objects.create(**validated_data)
def update(self, instance, validated_data):
        instance.userId = validated_data.get('userId', instance.userId)
        instance.firstName = validated_data.get('userId', instance.firstName)
        instance.lastName = validated_data.get('userId', instance.lastName)
        instance.imgurl = validated_data.get('userId', instance.imgurl)
        instance.phone_number = validated_data.get('userId', instance.phone_number)
        instance.email = validated_data.get('userId', instance.email)
        instance.userType = validated_data.get('userId', instance.userType)
        instance.lat = validated_data.get('userId', instance.lat)
        instance.lng = validated_data.get('userId', instance.lng)
        instance.password = validated_data.get('userId', instance.password)
       


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = '__all__'
def create(self , validated_data):
    return VehicleModel.objects.create(**validated_data)