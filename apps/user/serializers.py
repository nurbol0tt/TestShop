from rest_framework import serializers

from apps.user.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        instance.set_password(password)
        instance.save()
        return instance


# class CustomJSONWebTokenAPIView(JSONWebTokenAPIView):
#     serializer_class = JSONWebTokenSerializer
#
#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)
#         if response.status_code == status.HTTP_200_OK:
#             # Добавьте дополнительные данные, которые вы хотите вернуть при успешном логине
#             user = self.serializer.validated_data['user']
#             payload = jwt_payload_handler(user)
#             token = jwt_encode_handler(payload)
#             response.data['token'] = token
#         return response
