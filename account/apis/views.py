from django.contrib import auth
from django.http import HttpResponse
from rest_framework import generics, permissions, serializers
from rest_framework.response import Response
from knox.models import AuthToken
from account.apis.serializers import UserSerializer, RegisterSerializer, LoginSerializer
from django.contrib.auth.models import User


class UsersApiView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer


class UsersDetailsApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SignUpAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = AuthToken.objects.create(user)
        return Response(
            {
                "users": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": token[1],
            }
        )


class SignInAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )
