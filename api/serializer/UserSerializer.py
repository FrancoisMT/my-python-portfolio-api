from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from ..models import User;

class UserSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = User
        fields = ['mail', 'password']

    def create(self, validated_data):
        hashPwd = make_password(validated_data['password'])
        user = User(mail=validated_data['mail'], password = hashPwd)
        user.save()

    def get_login_response(self):
        response = self.data
        response.pop('password')
        return response