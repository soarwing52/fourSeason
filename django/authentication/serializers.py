import email
from django.contrib.auth.models import User, Group
from rest_framework import serializers

from activities.models import Activity


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    activities = serializers.PrimaryKeyRelatedField(many=True, required=False, queryset=Activity.objects.all(), allow_null=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password','email', 'first_name', 'last_name', 'activities']

    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({'email', ('Email already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    username = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['username', 'password']