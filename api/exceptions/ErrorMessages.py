from .ErrorCode import ErrorCode
from rest_framework import status

error_message = {
    ErrorCode.INVALID_CREDENTIALS: {'status': status.HTTP_400_BAD_REQUEST, 'message': 'Idenfiants invalides'},
    ErrorCode.SERVER_ERROR: {'status': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': 'Internal Server Error'},
    ErrorCode.MISSING_PARAMETERS: {'status': status.HTTP_400_BAD_REQUEST, 'message': 'Paramètres manquants'}
}
