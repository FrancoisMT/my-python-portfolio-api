import datetime
from django.conf import settings
import jwt
from rest_framework.exceptions import AuthenticationFailed
from api.models import User
import environ 
env=environ.Env()
environ.Env.read_env()

class JwtService:

    @staticmethod
    def generate_token(user_id):
        expiration_time = datetime.datetime.utcnow() + datetime.timedelta(seconds=int(env('TOKEN_EXPIRATION_SECONDS')))
        payload = {
            'user_id': user_id,
            'exp': expiration_time,
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, env('SECRET_KEY'), algorithm='HS256')
        return token
    
    @staticmethod
    def decode_token(token):
        try:
            payload = jwt.decode(token, env('SECRET_KEY'), algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token expired")
        except jwt.InvalidTokenError:
            raise AuthenticationFailed("Invalid token")

    @staticmethod
    def check_role(user_id, required_role):
        try:
            user = User.objects.get(id=user_id)
            if user.role != required_role:
                raise AuthenticationFailed(f"User does not have the required role: {required_role}")
        except User.DoesNotExist:
            raise AuthenticationFailed("User not found")