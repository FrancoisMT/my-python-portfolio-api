from rest_framework.exceptions import APIException
from .ErrorCode import ErrorCode

class CustomApiException(APIException):

    def __init__(self, status_code, error_code: ErrorCode, message:str):
        self.status_code = status_code
        self.default_code = error_code
        super().__init__(detail={'message': message})