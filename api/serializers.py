from rest_framework import serializers
from .models import User, AdminContent

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'mobile_number', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            full_name=validated_data['full_name'],
            mobile_number=validated_data['mobile_number']
        )


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid credentials")

        if not user.check_password(data['password']):
            raise serializers.ValidationError("Invalid credentials")

        return user


class AdminContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminContent
        fields = '__all__'
