from rest_framework import mixins, filters
from blood.mblood.api.serializers import *
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend

from blood.mblood.models import Donor
from blood.core.api.viewsets import BaseModelViewSet

'''from django_filters.rest_framework import DjangoFilterBackend'''


class DonorViewSet(BaseModelViewSet, mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.CreateModelMixin, ):
    queryset = Donor.objects.filter(is_active=True)
    serializer_class = BloodBankSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_field = {

        "name": ['exact', 'contains'],
        "surname": ['exact', 'contains'],
        "sex": ['exact', 'contains'],
        "age": ['exact', 'contains'],
        "phone_number": ['exact', 'contains'],
        "date": ['exact', 'contains'],
        "email": ['exact', 'contains'],
        "blood_group": ['exact', 'contains'],
        "password": ['exact', 'contains'],
        # "updated_at": ['gte', 'lte', 'exact', 'gt', 'lt'],
        # "created_at": ['gte', 'lte', 'exact', 'gt', 'lt']
    }
    search_fields = ["name", "address"]
    ordering_fields = ["surname", "name", "date"]
    order = ["surname", "name", "date"]
    ordering = ["surname", "name", "date"]
    parser_classes = [FormParser, MultiPartParser, JSONParser]


class CampaignViewSet(BaseModelViewSet, mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.CreateModelMixin, ):
    queryset = Donor.objects.filter(is_active=True)
    serializer_class = BloodBankSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_field = {

        "name": ['exact', 'contains'],
        "start_date": ['exact', 'contains'],
        "end_date": ['exact', 'contains'],
        "email": ['exact', 'contains']
        # "updated_at": ['gte', 'lte', 'exact', 'gt', 'lt'],
        # "created_at": ['gte', 'lte', 'exact', 'gt', 'lt']
    }
    search_fields = ["name", "start_date", "end_date", "email"]
    ordering_fields = ["name", "start_date", "end_date", "email"]
    order = ["name"]
    ordering = ["name"]
    parser_classes = [FormParser, MultiPartParser, JSONParser]


class AffiliationViewSet(BaseModelViewSet, mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.CreateModelMixin, ):
    queryset = Donor.objects.filter(is_active=True)
    serializer_class = BloodBankSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_field = {

        "donor": ['exact', 'contains'],
        "campaign": ['exact', 'contains'],
        # "updated_at": ['gte', 'lte', 'exact', 'gt', 'lt'],
        # "created_at": ['gte', 'lte', 'exact', 'gt', 'lt']
    }
    search_fields = ["donor", "campaign"]
    ordering_fields = ["donor", "campaign"]
    order = ["name"]
    ordering = ["name"]
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
        "quantity": ['exact', 'contains']
    }
    search_fields = ["blood_group", "quantity"]
    ordering_fields = ["blood_group", "quantity"]
    order = ["blood_group", "quantity"]
    ordering = ["blood_group", "quantity"]
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
        "Expiration": ['exact', 'contains'],
        "donor": ['exact', 'contains'],
        "blood_bank": ['extract', 'contains']

        # "updated_at": ['gte', 'lte', 'exact', 'gt', 'lt'],
        # "created_at": ['gte', 'lte', 'exact', 'gt', 'lt']
    }
    search_fields = ["quantity", "Expiration", "donor", "blood_bank"]
    ordering_fields = ["quantity", "Expiration", "donor"]
    order = ["quantity", "Expiration", "donor"]
    ordering = ["quantity", "Expiration", "donor"]
    parser_classes = [FormParser, MultiPartParser, JSONParser]


class BloodTypeViewSet(BaseModelViewSet, mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.CreateModelMixin, ):
    queryset = BloodType.objects.filter(is_active=True)
    serializer_class = BloodTypeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_field = {

        "quantity": ['exact', 'contains']

        # "updated_at": ['gte', 'lte', 'exact', 'gt', 'lt'],
        # "created_at": ['gte', 'lte', 'exact', 'gt', 'lt']
    }
    '''
    search_fields = ["quantity"]
    ordering_fields = ["quantity"]
    order = ["quantity"]
    ordering = ["quantity"]
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
        "blood_type": ['exact', 'contains'],
        "blood_bank": ['exact', 'contains'],
        # "updated_at": ['gte', 'lte', 'exact', 'gt', 'lt'],
        # "created_at": ['gte', 'lte', 'exact', 'gt', 'lt']
    }
    search_fields = ["quantity", "blood_type", "blood_bank"]
    ordering_fields = ["quantity"]
    order = ["quantity"]
    ordering = ["quantity"]
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
        "hospital": ['exact', 'contains'],
        "password": ['exact', 'contains']

        # "updated_at": ['gte', 'lte', 'exact', 'gt', 'lt'],
        # "created_at": ['gte', 'lte', 'exact', 'gt', 'lt']
    }
    search_fields = ["name", "surname", "email", "hospital"]
    ordering_fields = ["name", "surname", "sex", "phone_number", "email", "hospital", "password"]
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

        "name": ['exact', 'contains'],
        "surname": ['exact', 'contains'],
        "sex": ['exact', 'contains'],
        "phone_number": ['exact', 'contains'],
        "email": ['exact', 'contains'],
        "blood_type": ['exact', 'contains'],
        "users": ['exact', 'contains']

        # "updated_at": ['gte', 'lte', 'exact', 'gt', 'lt'],
        # "created_at": ['gte', 'lte', 'exact', 'gt', 'lt']
    }
    search_fields = ["name", "surname", "sex", "phone_number", "email", "blood_type", "users"]
    ordering_fields = ["name", "surname", "sex", "phone_number", "email", "blood_type", "users"]
    order = ["name", "surname", "sex", "phone_number", "email", "blood_type", "users"]
    ordering = ["name", "surname", "sex", "phone_number", "email", "blood_type", "users"]
    parser_classes = [FormParser, MultiPartParser, JSONParser]
