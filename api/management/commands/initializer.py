from django.core.management.base import BaseCommand
from ...models.User import User
from django.contrib.auth.hashers import make_password
import environ 
env=environ.Env()
environ.Env.read_env()

class Command(BaseCommand):
    def handle(self,*args, **kwargs):
        admin_mail=env('ADMIN_MAIL')
        admin_pwd=env('ADMIN_PASSWORD')

        try:
            User.objects.get(mail=admin_mail)
            print("USER ALREADY EXISTS")
        except User.DoesNotExist:
            print("USER NOT EXISTS")
            save_admin = User.objects.create(mail=admin_mail, password=make_password(admin_pwd))
        except Exception as e:
            print(str(e))
    

    
        