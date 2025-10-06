from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from blood.mblood.models import BloodDonation


@receiver(post_save, sender=BloodDonation)
def update_donor_last_donation_date(sender, instance, created, **kwargs):
    """
    Met automatiquement à jour la date du dernier don
    dès qu'un nouveau BloodDonation est créé.
    """
    if created and instance.donor:
        instance.donor.last_donation_date = timezone.now().date()
        instance.donor.save(update_fields=["last_donation_date"])
