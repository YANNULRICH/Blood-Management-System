from rest_framework import serializers

from blood.core.api.serializers import BaseSerializer
from blood.mblood.models import Donor, BloodDonation, BloodType, BloodBag, Hospital, Users, Command, BloodBank, \
    Campaign, Affiliation


class DonorSerializer(BaseSerializer):
    class Meta:
        model = Donor
        fields = ("id", "name", "surname", "sex", "age", "phone_number", "date", "email", "password")


class CampaignSerializer(BaseSerializer):
    class Meta:
        model = Campaign
        fields = ("id", "name", "start_date", "end_date", "email")


class AffiliationSerializer(BaseSerializer):
    class Meta:
        model = Affiliation
        fields = ("id", "donor", "campaign")


class BloodBankSerializer(BaseSerializer):
    class Meta:
        model = BloodBank
        fields = ("id", "blood_group", "code", "name")


class BloodDonationSerializer(BaseSerializer):
    class Meta:
        model = BloodDonation
        fields = ("id", "Expiration_date", "quantity", "donor", "blood_bank")


class BloodTypeSerializer(BaseSerializer):
    class Meta:
        model = BloodType
        fields = ("id", "code")


class BloodBagSerializer(BaseSerializer):
    class Meta:
        model = BloodBag
        fields = ("id", "quantity", "blood_type", "blood_bank", "code")


class HospitalSerializer(BaseSerializer):
    class Meta:
        model = Hospital
        fields = ("id", "name","address", "email", "phone_number")


class UsersSerializer(BaseSerializer):
    class Meta:
        model = Users
        fields = ("id", "name", "surname", "sex", "phone_number", "email", "hospital", "password")


class CommandSerializer(BaseSerializer):
    class Meta:
        model = Command
        fields = ("id", "command_number", "quantity", "users", "blood_type", "code")
