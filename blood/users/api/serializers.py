import logging

from django.contrib.auth.models import Group, Permission
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from blood.core.api.serializers import BaseSerializer
from blood.users.models import User
from blood.utils.randomize_digit_char import randomize_digit_char_code


def generate_user_code():
    """"""
    user_code = randomize_digit_char_code(N=4)
    exist_user = User.objects.filter(is_active=True, user_code=user_code).exists()
    if exist_user:
        return generate_user_code()
    return user_code


logger_users = logging.getLogger('users_logger')


class PermissionSerializer(BaseSerializer):
    """
    Serializer for Permission.
    """

    code = serializers.SerializerMethodField()

    class Meta:
        model = Permission
        fields = ["id", "name", "code"]

    def get_code(self, obj) -> str:
        return f"{obj.content_type.app_label}.{obj.codename}"


class GroupSerializer(BaseSerializer):
    """
    Serializer for Group.
    """

    class Meta:
        model = Group
        fields = ["id", "name", "permissions"]


class UserSerializer(BaseSerializer):
    class Meta:
        model = User
        fields = (
            "id", "is_active", "email", "password", "phone_number", "first_name", "last_name",
            "gender","profile_picture_file")
        extra_kwargs = {"password": {"write_only": True}}


class CreateUserSerializer(BaseSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "is_active",
            "email",
            "phone_number",
            "first_name",
            "last_name",
            "gender",
            "user_code",
            "profile_picture_file",
            "password",
            "groups",
            "user_permissions",
        )
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = ["user_code"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        logger_users.info(f'{user.email} just created by {self.context["request"].user.email}')
        user.set_password(password)
        user.user_code = generate_user_code()
        user.save()
        return user


class UserDetailSerializer(BaseSerializer):
    groups = GroupSerializer(many=True)
    user_permissions = PermissionSerializer(many=True)
    permissions = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "is_active",
            "email",
            "phone_number",
            "first_name",
            "last_name",
            "gender",
            "user_code",
            "profile_picture_file",
            "password",
            "user_permissions",
            "groups",
            "permissions",

        )
        extra_kwargs = {"password": {"write_only": True}}
        depth = 1

    def get_permissions(self, obj):
        user_permissions = obj.get_user_permissions()
        groups = obj.groups.all()
        for group in groups:
            permissions = group.permissions.all()
            for permission in permissions:
                perm = f"{permission.content_type.app_label}.{permission.codename}"
                if perm not in user_permissions:
                    user_permissions.add(perm)
        return user_permissions


class SelfPasswordSerializer(BaseSerializer):
    old_password = serializers.CharField()

    class Meta:
        model = User
        fields = ("old_password", "password")
        extra_kwargs = {
            "password": {"write_only": True},
            "old_password": {"write_only": True},
        }

    def validate_old_password(self, value):
        if not self.context.get("request").user.check_password(value):
            raise ValidationError("Old password is invalid.")

        return value

    def save(self):
        user = self.context.get("request").user
        user.set_password(self.validated_data["password"])
        user.save()


class PasswordSerializer(BaseSerializer):
    class Meta:
        model = User
        fields = ("password",)
        extra_kwargs = {"password": {"write_only": True}}

    def save(self):
        user = self.instance
        user.set_password(self.validated_data["password"])
        user.save()


class TokenObtainLifetimeSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        username = self.user.email
        refresh = self.get_token(self.user)
        data['lifetime'] = int(refresh.access_token.lifetime.total_seconds())
        logger_users.info(f'{username} just connected')
        return data


class TokenRefreshLifetimeSerializer(TokenRefreshSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = RefreshToken(attrs['refresh'])
        data['lifetime'] = int(refresh.access_token.lifetime.total_seconds())
        return data
