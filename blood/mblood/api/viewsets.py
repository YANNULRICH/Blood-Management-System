from rest_framework import mixins, filters
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend

from blood.mblood.api.serializers import BloodBankSerializer, BloodDonationSerializer, BloodTypeSerializer, \
    BloodBagSerializer, HospitalSerializer, UsersSerializer, CommandSerializer, DonorSerializer
from blood.mblood.models import Donor, BloodBank, BloodDonation, BloodType, BloodBag, Hospital, Users, Command
from blood.core.api.viewsets import BaseModelViewSet

'''from django_filters.rest_framework import DjangoFilterBackend'''


class DonorViewSet(BaseModelViewSet, mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.CreateModelMixin, ):
    queryset = Donor.objects.filter(is_active=True)
    serializer_class = DonorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_field = {

        "name": ['exact', 'contains'],
        "sex": ['exact', 'contains'],
        "phone_number": ['exact', 'contains'],
        "surname": ['exact', 'contains'],
        "date": ['exact', 'contains'],
        "age": ['exact', 'contains'],
        "email": ['exact', 'contains'],
        "blood_group": ['exact', 'contains'],
        "password": ['exact', 'contains']
        # "updated_at": ['gte', 'lte', 'exact', 'gt', 'lt'],
        # "created_at": ['gte', 'lte', 'exact', 'gt', 'lt']
    }
    search_fields = ["name", "address", "phone_number", "surname", "date", "age", "email", "blood_group"]
    ordering_fields = ["surname", "name", "date"]
    order = ["surname", "name", "date"]
    ordering = ["surname", "name", "date"]
    parser_classes = [FormParser, MultiPartParser, JSONParser]


class BloodBankViewSet(BaseModelViewSet, mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.CreateModelMixin, ):
    queryset = BloodBank.objects.filter(is_active=True)
    serializer_class = BloodBankSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_field = {

        "blood_group": ['exact', 'contains'],
        "quantity": ['exact', 'contains'],
        "code": ['exact', 'contains']
    }
    search_fields = ["blood_group", "quantity", "code"]
    ordering_fields = ["blood_group", "quantity", "code"]
    order = ["blood_group", "quantity", "code"]
    ordering = ["blood_group", "quantity", "code"]
    parser_classes = [FormParser, MultiPartParser, JSONParser]


class BloodDonationViewSet(BaseModelViewSet, mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.CreateModelMixin, ):
    queryset = BloodDonation.objects.filter(is_active=True)
    serializer_class = BloodDonationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_field = {

        "quantity": ['exact', 'contains'],
        "Expiration_date": ['exact', 'contains'],
        "donor": ['exact', 'contains'],
        "blood_bank": ['extract', 'contains']
        # "updated_at": ['gte', 'lte', 'exact', 'gt', 'lt'],
        # "created_at": ['gte', 'lte', 'exact', 'gt', 'lt']
    }
    search_fields = ["quantity", "Expiration_date", "donor", "blood_bank"]
    ordering_fields = ["quantity", "Expiration_date", "donor"]
    order = ["quantity", "Expiration_date", "donor"]
    ordering = ["quantity", "Expiration_date", "donor"]
    parser_classes = [FormParser, MultiPartParser, JSONParser]


class BloodTypeViewSet(BaseModelViewSet, mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.CreateModelMixin, ):
    queryset = BloodType.objects.filter(is_active=True)
    serializer_class = BloodTypeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_field = {

        "code": ['exact', 'contains'],
        "quantity": ['exact', 'contains']
        # "updated_at": ['gte', 'lte', 'exact', 'gt', 'lt'],
        # "created_at": ['gte', 'lte', 'exact', 'gt', 'lt']
    }
    '''
    search_fields = ["quantity", "code"]
    ordering_fields = ["code"]
    order = ["code"]
    ordering = ["code"]
    '''
    parser_classes = [FormParser, MultiPartParser, JSONParser]


class BloodBagViewSet(BaseModelViewSet, mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.CreateModelMixin, ):
    queryset = BloodBag.objects.filter(is_active=True)
    serializer_class = BloodBagSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_field = {

        "quantity": ['exact', 'contains'],
        "code": ['exact', 'contains'],
        "blood_type": ['exact', 'contains'],
        "blood_bank": ['exact', 'contains']
        # "updated_at": ['gte', 'lte', 'exact', 'gt', 'lt'],
        # "created_at": ['gte', 'lte', 'exact', 'gt', 'lt']
    }
    search_fields = ["quantity", "blood_type", "blood_bank", "code"]
    ordering_fields = ["quantity", "code"]
    order = ["quantity", "code"]
    ordering = ["quantity", "code"]
    parser_classes = [FormParser, MultiPartParser, JSONParser]


class HospitalViewSet(BaseModelViewSet, mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.CreateModelMixin, ):
    queryset = Hospital.objects.filter(is_active=True)
    serializer_class = HospitalSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_field = {

        "address": ['exact', 'contains'],
        "email": ['exact', 'contains'],
        "phone_number": ['exact', 'contains']
        # "updated_at": ['gte', 'lte', 'exact', 'gt', 'lt'],
        # "created_at": ['gte', 'lte', 'exact', 'gt', 'lt']
    }
    search_fields = ["address", "email"]
    ordering_fields = ["address", "email", "phone_number"]
    order = ["address", "email", "phone_number"]
    ordering = ["address", "email", "phone_number"]
    parser_classes = [FormParser, MultiPartParser, JSONParser]


class UsersViewSet(BaseModelViewSet, mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.CreateModelMixin, ):
    queryset = Users.objects.filter(is_active=True)
    serializer_class = UsersSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_field = {

        "name": ['exact', 'contains'],
        "surname": ['exact', 'contains'],
        "sex": ['exact', 'contains'],
        "phone_number": ['exact', 'contains'],
        "email": ['exact', 'contains'],
        # "password": ['exact', 'contains'],
        "hospital": ['exact', 'contains']
        # "updated_at": ['gte', 'lte', 'exact', 'gt', 'lt'],
        # "created_at": ['gte', 'lte', 'exact', 'gt', 'lt']
    }
    search_fields = ["name", "surname", "email", "hospital", "password"]
    ordering_fields = ["name", "surname", "sex", "phone_number", "email", "hospital"]
    order = ["name", "surname", "sex", "phone_number", "email", "hospital"]
    ordering = ["name", "surname", "sex", "phone_number", "email", "hospital"]
    parser_classes = [FormParser, MultiPartParser, JSONParser]


class CommandViewSet(BaseModelViewSet, mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.CreateModelMixin, ):
    queryset = Command.objects.filter(is_active=True)
    serializer_class = CommandSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_field = {

        "command_number": ['exact', 'contains'],
        "quantity": ['exact', 'contains'],
        "blood_type": ['exact', 'contains'],
        "users": ['exact', 'contains'],
        "code": ['exact', 'contains']
        # "updated_at": ['gte', 'lte', 'exact', 'gt', 'lt'],
        # "created_at": ['gte', 'lte', 'exact', 'gt', 'lt']
    }
    search_fields = ["command_number", "quantity", "blood_type", "users", "code"]
    ordering_fields = ["command_number", "quantity", "blood_type", "users"]
    order = ["command_number", "quantity", "blood_type", "users"]
    ordering = ["command_number", "quantity", "blood_type", "users"]
    parser_classes = [FormParser, MultiPartParser, JSONParser]
