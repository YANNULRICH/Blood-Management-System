from django.db import models

from blood.core.models import BaseModel


class Donor(BaseModel):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.IntegerField(unique=True)
    date = models.DateTimeField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    blood_group = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, unique=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.is_active}"


class BloodBank(BaseModel):
    quantity = models.CharField(max_length=100, null=True)
    blood_group = models.CharField(max_length=100)
    code = models.CharField(max_length=100, unique=True, default="A")


class BloodDonation(BaseModel):
    Expiration_date = models.DateTimeField(max_length=100, null=True)
    quantity = models.CharField(max_length=100)
    donor = models.ForeignKey(Donor,
                              on_delete=models.CASCADE,
                              null=False,
                              related_name="blood_donation")
    blood_bank = models.ForeignKey(BloodBank,
                                   on_delete=models.CASCADE,
                                   null=False,
                                   related_name="blood_donation")


class BloodType(BaseModel):
    quantity = models.CharField(max_length=100, null=True)
    code = models.CharField(max_length=100, unique=True, default="A")


class BloodBag(BaseModel):
    quantity = models.CharField(max_length=100)
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
    # password = models.CharField(max_length=128, unique=True)
    hospital = models.ForeignKey(Hospital,
                                 on_delete=models.CASCADE,
                                 null=False,
                                 related_name="users")


class Command(BaseModel):
    command_number = models.IntegerField(unique=True)
    quantity = models.CharField(max_length=100)
    code = models.CharField(max_length=100, default="A")
    users = models.ForeignKey(Users,
                              on_delete=models.CASCADE,
                              null=False,
                              related_name="command")
    blood_type = models.ForeignKey(BloodType,
                                   on_delete=models.CASCADE,
                                   null=False,
                                   related_name="blood_command")


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
