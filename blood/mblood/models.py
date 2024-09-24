import uuid

from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from blood.core.models import BaseModel
from blood.utils.random import generate_unique_code, generate_code


class Donor(BaseModel):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.IntegerField(unique=True)
    date = models.DateTimeField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    blood_group = models.CharField(max_length=100, unique=False, default="")
    password = models.CharField(max_length=100, unique=True, default="")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.is_active}"


class Campaign(BaseModel):
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    email = models.EmailField(max_length=100, unique=True)


class Affiliation(BaseModel):
    campaign = models.ForeignKey(Campaign,
                                 on_delete=models.CASCADE,
                                 null=False,
                                 related_name="affiliation")
    donor = models.ForeignKey(Donor,
                              on_delete=models.CASCADE,
                              null=False,
                              related_name="affiliation")


class BloodBank(BaseModel):
    blood_group = models.CharField(max_length=100)
    code = models.CharField(max_length=100, unique=True, blank=True)
    name = models.CharField(max_length=100, default="A")


'''
@receiver(post_save, sender=BloodBank)
def generate_code(sender, instance, created, **kwargs):
    if created:
        random_part = generate_random_code()
        instance.code = f"blbk_{instance.name}_{random_part}"
        instance.save()
'''


class BloodDonation(BaseModel):
    Expiration_date = models.DateTimeField(max_length=100, null=True)
    quantity = models.IntegerField()
    donor = models.ForeignKey(Donor,
                              on_delete=models.CASCADE,
                              null=False,
                              related_name="blood_donation")
    blood_bank = models.ForeignKey(BloodBank,
                                   on_delete=models.CASCADE,
                                   null=False,
                                   related_name="blood_donation")


class BloodType(BaseModel):
    code = models.CharField(max_length=100, unique=True, default="A")


class BloodBag(BaseModel):
    quantity = models.IntegerField()
    code = models.CharField(max_length=100, default="A")
    blood_bank = models.ForeignKey(BloodBank,
                                   on_delete=models.CASCADE,
                                   null=False,
                                   related_name="blood_bag")

    blood_type = models.ForeignKey(BloodType,
                                   on_delete=models.CASCADE,
                                   null=False,
                                   related_name="blood_bag")


class Hospital(BaseModel):
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.IntegerField(unique=True)


class Users(BaseModel):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    phone_number = models.IntegerField(unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100, unique=True, default="")
    hospital = models.ForeignKey(Hospital,
                                 on_delete=models.CASCADE,
                                 null=False,
                                 related_name="users")


class Command(BaseModel):
    command_number = models.IntegerField(unique=True)
    quantity = models.IntegerField()
    code = models.CharField(max_length=100, unique =True)
    users = models.ForeignKey(Users,
                              on_delete=models.CASCADE,
                              null=False,
                              related_name="command")
    blood_type = models.ForeignKey(BloodType,
                                   on_delete=models.CASCADE,
                                   null=False,
                                   related_name="blood_command")


@receiver(post_save, sender=BloodBank)
@receiver(post_save, sender=BloodBag)
@receiver(post_save, sender=Command)
def generate_code(sender, instance, created, **kwargs):
    if created:
        instance.code = generate_unique_code(instance)
        instance.save()


'''
    class Meta:
        ordering = ["created_at"]
        verbose_name = _("country")
        verbose_name = _("countries")
        indexes = [
            models.Index(fields=["code"], name = "country_code_idx"),
        ]

    def __str__(self):
        return f"{self.code} - {self.name}"


class donor:
    name =models.CharField(_())
'''
