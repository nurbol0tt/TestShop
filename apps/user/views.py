from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user.serializers import UserRegisterSerializer


class RegisterView(APIView):
    serializer_class = UserRegisterSerializer

    def post(self, request) -> Response:
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "User registered successfully"},
            status=status.HTTP_201_CREATED,
        )
