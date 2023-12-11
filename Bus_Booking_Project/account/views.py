from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.http import JsonResponse
from rest_framework import status
from rest_framework.authtoken.admin import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def user_signup(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = {"response":serializer.data}
            return Response(context)
        else:
            return Response({"error":"information is  is not VALID"})

    else:
        return Response({'error':"Invalid HTTP method"})

@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh_token": str(refresh),
                "access_token": str(refresh.access_token)
            })
        else:
            return Response({'error': 'Password or username is incorrect.'}, status=status.HTTP_401_UNAUTHORIZED)

    return Response({'error': 'Invalid HTTP method.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def user_logout(request):
    logout(request)
    return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)



