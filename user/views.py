from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import (RegisterValidateSerializer, AuthValidateSerializer, ConfirmSerializer)
from .models import ConfirmationCode
import random


@api_view(['POST'])
def registration_api_view(request):
    serializer = RegisterValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data['username']
    password = serializer.validated_data['password']

    user = User.objects.create_user(
        username=username,
        password=password,
        is_active=False
    )

    code = str(random.randint(100000, 999999))

    ConfirmationCode.objects.create(
        user=user,
        code=code
    )

    return Response(
        status=status.HTTP_201_CREATED,
        data={'user_id': user.id,'code': code}
    )

@api_view(['POST'])
def confirm_api_view(request):
    serializer = ConfirmSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data['username']
    code = serializer.validated_data['code']

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response(
            status=status.HTTP_404_NOT_FOUND
        )

    try:
        confirmation_code = ConfirmationCode.objects.get(user=user)
    except ConfirmationCode.DoesNotExist:
        return Response(
            status=status.HTTP_404_NOT_FOUND
        )

    if confirmation_code.code == code:
        user.is_active = True
        user.save()


        return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST) 


@api_view(['POST'])
def authorization_api_view(request):
    serializer = AuthValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = authenticate(**serializer.validated_data)

    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            data={'key': token.key},
            status=status.HTTP_200_OK
        )

    return Response(status=status.HTTP_401_UNAUTHORIZED)