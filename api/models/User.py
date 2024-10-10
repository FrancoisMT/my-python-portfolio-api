from django.db import models
from django.contrib.auth.hashers import check_password
from ..exceptions import CustomException, ErrorCode

class User(models.Model):
    mail=models.CharField(max_length=50)
    password=models.CharField(max_length=256)
    
    def check_pwd(self, clear_pwd) -> bool:

        if check_password(clear_pwd, self.password):
            return True
        
        raise CustomException(ErrorCode.INVALID_CREDENTIALS)
    