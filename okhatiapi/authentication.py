# authentication.py
from rest_framework import authentication
from rest_framework import exceptions
from django.contrib.auth.models import User

class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.META.get('HTTP_USERNAME')
        if not username:
            return None
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')
        return (user, None)
