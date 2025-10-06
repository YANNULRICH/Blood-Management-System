from collections import Counter

from django.db import OperationalError
from django.db.models import Count, Sum
from django.http import JsonResponse
from rest_framework import mixins, filters, status, response, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from blood.core import models
from blood.mblood.api.serializers import BloodBankSerializer, BloodDonationSerializer, BloodTypeSerializer, \
    BloodBagSerializer, HospitalSerializer, UsersSerializer, CommandSerializer, DonorSerializer, CampaignSerializer, \
    AffiliationSerializer
from blood.mblood.models import Donor, BloodBank, BloodDonation, BloodType, BloodBag, Hospital, Users, Command, \
    Affiliation, Campaign
from blood.core.api.viewsets import BaseModelViewSet

'''from django_filters.rest_framework import DjangoFilterBackend'''


class DonorViewSet(BaseModelViewSet,
            viewsets.GenericViewSet,
               mixins.ListModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.CreateModelMixin, ):
    queryset = Donor.objects.filter(is_active=True)
    serializer_class = DonorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {

        "name": ['exact', 'contains'],
        "sex": ['exact', 'contains'],
        "phone_number": ['exact', 'contains'],
        "surname": ['exact', 'contains'],
        "age": ['exact', 'contains'],
        "email": ['exact', 'contains'],
        "blood_group": ['exact', 'contains'],
        "updated_at": ['gte', 'lte', 'exact', 'gt', 'lt'],
        "created_at": ['gte', 'lte', 'exact', 'gt', 'lt'],
        "last_donation_date": ['exact', 'gte', 'lte'],
    }
    search_fields = ["name", "address", "phone_number", "surname", "age", "email", "blood_group"]
    ordering_fields = ["surname", "name"]
    order = ["surname", "name"]
    ordering = ["surname", "name"]
    parser_classes = [FormParser, MultiPartParser, JSONParser]


class CampaignViewSet(BaseModelViewSet, mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.CreateModelMixin, ):
    queryset = Campaign.objects.filter(is_active=True)
    serializer_class = CampaignSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_field = {

        "name": ['exact', 'contains'],
        "location": ['exact', 'contains'],
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
    queryset = Affiliation.objects.filter(is_active=True)
    serializer_class = AffiliationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_field = {

        "donor": ['exact', 'contains'],
        "campaign": ['exact', 'contains'],
        # "updated_at": ['gte', 'lte', 'exact', 'gt', 'lt'],
        # "created_at": ['gte', 'lte', 'exact', 'gt', 'lt']
    }
    search_fields = ["donor", "campaign"]
    ordering_fields = ["donor", "campaign"]
    order = ["campaign"]
    ordering = ["campaign"]
    parser_classes = [FormParser, MultiPartParser, JSONParser]


class BloodBankViewSet(BaseModelViewSet, mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.CreateModelMixin, ):
    lookup_field = 'id'
    queryset = BloodBank.objects.filter(is_active=True)
    serializer_class = BloodBankSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_field = {

        "blood_group": ['exact', 'contains'],
        "code": ['exact', 'contains'],
        "name": ['exact', 'contains']
    }
    search_fields = ["blood_group", "code"]
    ordering_fields = ["blood_group", "code"]
    order = ["blood_group", "code"]
    ordering = ["blood_group", "code"]
    parser_classes = [FormParser, MultiPartParser, JSONParser]

    @action(detail=True, methods=['get'])
    def blood_bag_summary(self, request, *args, **kwargs):
        blood_bank = self.get_object()

        try:
            # Fetch all related BloodBag records
            blood_bags = BloodBag.objects.filter(blood_bank=blood_bank)

            # Check if there are any BloodBag records
            if not blood_bags.exists():
                return Response({'detail': 'No BloodBag records found for this BloodBank.'},
                                status=status.HTTP_404_NOT_FOUND)

            # Aggregate BloodBags by blood type and sum their quantities
            summary = (blood_bags
                       .values('blood_type')
                       .annotate(total_quantity=Sum('quantity'))
                       .order_by('blood_type'))

            return Response(summary)

        except OperationalError as e:
            # Return a detailed error message for operational errors
            return Response({'detail': f'Database error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            # Return a detailed error message for any other exceptions
            return Response({'detail': f'Error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
        # "updated_at": ['gte', 'lte', 'exact', 'gt', 'lt'],
        # "created_at": ['gte', 'lte', 'exact', 'gt', 'lt']
    }
    '''
    search_fields = ["code"]
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
        "name": ['exact', 'contains'],
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
    search_fields = ["name", "surname", "email", "hospital", "password"]
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
