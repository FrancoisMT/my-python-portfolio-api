from rest_framework.decorators import api_view

from api.exceptions import ErrorCode
from api.services import JwtService
from api.validators.decorators import checkAdminRole
from ..serializer.UserSerializer import UserSerializer
from ..models import User
from rest_framework.response import Response
from rest_framework import status
from ..exceptions import CustomApiException, CustomException
from ..validators import check_body

@api_view(["POST"])
def login(request):

    try:

        check_body(request.data, ['mail', 'password'])

        user = User.objects.filter(mail=request.data['mail']).first()

        if user is None:  
            raise CustomException(ErrorCode.INVALID_CREDENTIALS)

        is_valid_pwd = user.check_pwd(clear_pwd=request.data['password'])

        if is_valid_pwd:
            token = JwtService.generate_token(user.id)
            return Response(data={"token": token, "user": user.mail}, status=status.HTTP_200_OK)

    except CustomException as ce:
        print(str(ce))
        raise ce.toApiException()
    except Exception as e:
        print(str(e))
        return Response(data="UNKNOWN_ERROR", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(["GET"])
@checkAdminRole
def admin_view(request):
    # Seul un ADMIN peut accéder à cette vue
    return Response({"message": "Bienvenue, administrateur !"}, status=status.HTTP_200_OK)