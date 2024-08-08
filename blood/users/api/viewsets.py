"""
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from blood.users.models import User

from .serializers import UserSerializer


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)
        """

import logging

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.decorators import action
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenViewBase
from blood.core.api.viewsets import BaseModelViewSet
from blood.users.api.serializers import UserSerializer, CreateUserSerializer, UserDetailSerializer, PasswordSerializer, \
    SelfPasswordSerializer, GroupSerializer, PermissionSerializer, TokenRefreshLifetimeSerializer, \
    TokenObtainLifetimeSerializer

User = get_user_model()
logger_users = logging.getLogger('users_logger')


class UserViewSet(
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    BaseModelViewSet,
):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["email", "password", "phone_number", "first_name", "last_name", "gender",
                        "user_code", "is_active",]
    search_fields = ["email", "phone_number", "first_name", "last_name", "register_number", "gender", "user_code"]
    ordering_fields = ["-updated_at", "-created_at", "email", "password", "phone_number", "gender"]
    ordering = ["-updated_at", "-created_at"]

    def get_serializer_class(self):
        if (
            self.action == "create"
            or self.action == "update"
            or self.action == "partial_update"
        ):
            return CreateUserSerializer

        if self.action == "retrieve":
            return UserDetailSerializer

        if self.action == "set-password":
            return PasswordSerializer

        if self.action == "set-my-password":
            return SelfPasswordSerializer

        return UserSerializer

    @action(detail=False, methods=["GET"])
    def get_ocs(self, request):
        queryset = self.get_queryset().filter(is_ocs=True)
        serializer = UserSerializer(queryset, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)

    @action(detail=False, methods=["GET"])
    def me(self, request):
        if request.method == "GET":
            serializer = UserDetailSerializer(
                request.user, context={"request": request}
            )
            return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=False, methods=["PUT"], url_path="set-my-password")
    def set_my_password(self, request):
        username = self.request.user.email
        serializer = SelfPasswordSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            logger_users.info(f'User {username} set is password')
            return Response(status=status.HTTP_200_OK, data={})
        logger_users.error(f'User {username} can not set is password')
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    @action(detail=True, methods=["PUT"], url_path="set-password")
    def set_user_password(self, request, *args, **kwargs):
        serializer = PasswordSerializer(
            self.get_object(), data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class TokenObtainPairView(TokenViewBase):
    """
        Return JWT tokens (access and refresh) for specific user based on username and password.
    """
    # throttle_classes = (UserLoginRateThrottle,)
    serializer_class = TokenObtainLifetimeSerializer


class TokenRefreshView(TokenViewBase):
    """
        Renew tokens (access and refresh) with new expire time based on specific user's access token.
    """
    serializer_class = TokenRefreshLifetimeSerializer


class PermissionViewSet(BaseModelViewSet, ListModelMixin):
    """
    ViewSet for listing permissions.
    """

    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["name", "codename"]
    search_fields = ["name", "codename"]
    ordering_fields = ["name", "codename"]


class GroupViewSet(
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    BaseModelViewSet,
):
    """
    ViewSet for creating, reading, updating and deleting groups.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["name", ]
    search_fields = ["name", ]
    ordering_fields = ["name", ]
