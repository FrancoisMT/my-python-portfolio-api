from .ErrorCode import ErrorCode
from .ErrorMessages import error_message
from .CustomApiException import CustomApiException

class CustomException(Exception):

    def __init__(self, error_code: ErrorCode, detail: str = None) -> None:
        self.error_code = error_code
        self.detail = detail

    def toApiException(self):
        data = error_message[self.error_code]
        print(self.error_code)
        
        return CustomApiException(
            status_code = data['status'],
            error_code=self.error_code.value,
            message = data['message']
        )