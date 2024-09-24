from collections import Counter

from django.db import OperationalError
from django.db.models import Count, Sum
from django.http import JsonResponse
from rest_framework import mixins, filters, status, response
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


class CampaignViewSet(BaseModelViewSet, mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.CreateModelMixin, ):
    queryset = Campaign.objects.filter(is_active=True)
    serializer_class = CampaignSerializer
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



'''

    @action(detail=True, methods=['get'])
    def classify_blood_bags(self, request, **kwargs):
        """
        Retrieves a BloodBank by ID, classifies its BloodBag objects by blood type,
        and calculates the total quantity for each blood type.

        Returns a dictionary with blood types as keys and their total quantities as values.
        """

        try:
            blood_bank = self.get_object()
        except BloodBank.DoesNotExist:
            return Response({'error': 'Blood Bank not found'}, status=404)

        blood_bags = BloodBag.objects.filter(blood_bank=blood_bank)

        blood_type_quantities = {}
        for blood_bag in blood_bags:
            blood_type = blood_bag.blood_group
            blood_type_quantities[blood_type] = blood_type_quantities.get(blood_type, 0) + blood_bag.quantity

        return Response(blood_type_quantities)
'''
'''
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


    @action(detail=True, methods=['get'], url_path='blood-bags-by-blood-group')
    def retrieve(self, request, pk=None, *args, **kwargs):
        blood_bank = get_object_or_404(self.queryset, pk=pk)
        serializer = self.get_serializer(blood_bank)
        # Get blood bags by blood bank (assuming a relation exists)
        blood_bags = blood_bank.bloodbag_set.all()  # Replace 'bloodbag_set' with the actual relation name
        blood_group_counts = blood_bags.values('blood_group').annotate(count=Count('blood_group'))

        response_data = {
            "blood_bank": serializer.data,
            "blood_group_counts": blood_group_counts
        }
        return Response(response_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='count-by-blood-group')
    def count_by_blood_group(self, request):
        try:
            blood_group_counts = BloodBank.objects.values('blood_group').annotate(count=Count('blood_group'))
            return Response(blood_group_counts, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get_quantity(self, request, pk=None):
        blood_bank = self.get_object()
        data = {
            'id': blood_bank.id,
            'quantity': blood_bank.quantity
        }
        return Response(data)

    @action(detail=True, methods=['get'])
    def get_quantity_by_group(self, request, pk=None):
        blood_bank = self.get_object()
        data = {
            'id': blood_bank.id,
            'blood_groups': {
                'A+': blood_bank.quantity_a_plus,
                'A-': blood_bank.quantity_a_minus,
                'B+': blood_bank.quantity_b_plus,
                'B-': blood_bank.quantity_b_minus,
                'AB+': blood_bank.quantity_ab_plus,
                'AB-': blood_bank.quantity_ab_minus,
                'O+': blood_bank.quantity_o_plus,
                'O-': blood_bank.quantity_o_minus,
            }
        }
        return JsonResponse(data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data = {
            'id': instance.id,
            'blood_group': {
                'A+': instance.quantity_a_plus,
                'A-': instance.quantity_a_minus,
                'B+': instance.quantity_b_plus,
                'B-': instance.quantity_b_minus,
                'AB+': instance.quantity_ab_plus,
                'AB-': instance.quantity_ab_minus,
                'O+': instance.quantity_o_plus,
                'O-': instance.quantity_o_minus
            }
        }
        return Response(data)
        '''


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
