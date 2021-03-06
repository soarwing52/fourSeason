from curses.ascii import US
from sys import prefix
import jwt
from django.conf import settings
from rest_framework import authentication, exceptions
from django.contrib.auth.models import User

class JWTAuthentication(authentication.BaseAuthentication):
    
    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)
        
        if not auth_data:
            return None

        prefix, token = auth_data.decode('utf-8').split(' ')
        print(token)
        print(settings.JWT_SECRET_KEY)
        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY)
            print(payload)
            user = User.objects.get(username=payload['username'])
            return (user, token)
        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed('token invalid')
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('token expired')


        return super().authenticate(request)
