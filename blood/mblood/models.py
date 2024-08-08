from django.db import models

from blood.core.models import BaseModel


class Donor(BaseModel):
    name = models.CharField(max_length=100, unique=False)
    surname = models.CharField(max_length=100, unique=False)
    sex = models.CharField(max_length=100, unique=False)
    age = models.IntegerField()
    phone_number = models.IntegerField()
    date = models.DateTimeField()
    email = models.EmailField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.is_active}"


class BloodBank(BaseModel):
    quantity = models.CharField(max_length=100, unique=False)
    blood_group = models.CharField(max_length=100, unique=False)


class BloodDonation(BaseModel):
    date = models.DateTimeField()
    quantity = models.CharField(max_length=100, unique=False)
    donor = models.ForeignKey(Donor,
                              on_delete=models.CASCADE,
                              null=False,
                              related_name="blood_donation")
    blood_bank = models.ForeignKey(BloodBank,
                                   on_delete=models.CASCADE,
                                   null=False,
                                   related_name="blood_donation")


class BloodType(BaseModel):
    quantity = models.CharField(max_length=100, unique=False)


class BloodBag(BaseModel):
    quantity = models.CharField(max_length=100, unique=False)
    blood_bank = models.ForeignKey(BloodBank,
                                   on_delete=models.CASCADE,
                                   null=False,
                                   related_name="blood_bag")

    blood_type = models.ForeignKey(BloodType,
                                   on_delete=models.CASCADE,
                                   null=False,
                                   related_name="blood_bag")


class Hospital(BaseModel):
    address = models.CharField()
    email = models.EmailField()
    phone_number = models.IntegerField()


class Users(BaseModel):
    name = models.CharField(max_length=100, unique=False)
    surname = models.CharField(max_length=100, unique=False)
    sex = models.CharField(max_length=100, unique=False)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=100, unique=True)
    hospital = models.ForeignKey(Hospital,
                                 on_delete=models.CASCADE,
                                 null=False,
                                 related_name="users")


class Command(BaseModel):
    command_number = models.IntegerField()
    quantity = models.CharField(max_length=100, unique=False)
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
