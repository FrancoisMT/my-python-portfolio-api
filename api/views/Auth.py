from rest_framework.decorators import api_view
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

        user = User.objects.get(mail=request.data['mail'])
        is_valid_pwd = user.check_pwd(clear_pwd=request.data['password'])

        if is_valid_pwd:
            serializer = UserSerializer(user)
            return Response(data=serializer.get_login_response(), status=status.HTTP_201_CREATED)

    except CustomException as ce:
        print(str(ce))
        raise ce.toApiException()
    except Exception as e:
        print(str(e))
        return Response(data="UNKNOWN_ERROR", status=status.HTTP_500_INTERNAL_SERVER_ERROR)