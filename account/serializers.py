from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}



class RegisterSerializizer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        user = Account.objects.create_user(validated_data['username'], validated_data['email'],
                                           validated_data['password'])

        return user


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        field = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Account.objects.log
