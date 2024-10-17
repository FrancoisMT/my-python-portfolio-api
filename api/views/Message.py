
from rest_framework.decorators import api_view

from api.exceptions import ErrorCode
from api.services import JwtService
from api.validators.decorators import checkAdminRole
from ..models import Message
from rest_framework.response import Response
from rest_framework import status
from ..exceptions import CustomException
from ..validators import check_body
from ..serializer import MessageSerializer

@api_view(["POST"])
def send(request):
    try:
        
        serializer = MessageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except CustomException as ce:
        print(str(ce))
        raise ce.toApiException()
    except Exception as e:
        print(str(e))
        return Response(data="UNKNOWN_ERROR", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
