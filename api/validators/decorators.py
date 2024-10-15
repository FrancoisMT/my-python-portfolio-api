from functools import wraps
from rest_framework.response import Response
from rest_framework import status

from api.services import JwtService

def check_role(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                return Response({"detail": "Authentication token required"}, status=status.HTTP_401_UNAUTHORIZED)

            try:
                # Décoder le token pour obtenir l'id de l'utilisateur
                payload = JwtService.decode_token(token.split(" ")[1])  # Le token est souvent sous la forme "Bearer <token>"
                user_id = payload['user_id']

                # Vérifier si l'utilisateur a le rôle requis
                JwtService.check_role(user_id, required_role)

                # Si tout va bien, continuer l'exécution de la fonction
                return func(request, *args, **kwargs)

            except Exception as e:
                return Response({"detail": str(e)}, status=status.HTTP_403_FORBIDDEN)

        return wrapper
    return decorator

def checkAdminRole(func):
    return check_role('ADMIN')(func)

def checkUserRole(func):
    return check_role('USER')(func)
