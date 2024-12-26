from rest_framework import serializers
from JLatorreASaravia.models import Compra

class ComprasSeriallizers(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = "__all__"

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)