from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics, status
# from .serializers import UserSerializer, ChangePasswordSerializer, UpdateProfileImageSerializer, UserDetailSerializer, UpdateUserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
# from .models import User
from rest_framework.response import Response
from rest_framework import status

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data,
                                            context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.username,
            })
        
        except ValidationError as e:
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)