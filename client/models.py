from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumber, PhoneNumberField
from .phone_number_validators import validate_possible_number
from django.utils.text import slugify


class PossiblePhoneNumberField(PhoneNumberField):
    default_validators = [validate_possible_number]


class Client(models.Model):
    account_number = models.CharField(max_length=255, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_user', null=True, blank=False)
    name = models.CharField(max_length=255)  # client name
    client_note = models.TextField(max_length=600, blank=True, null=True)
    # general
    company = models.CharField(max_length=600, blank=False, null=True)
    phone = PossiblePhoneNumberField(blank=True, default="")

    LICENSES = (
        (1, "Standard"),
        (2, "Enterprise"),
        (3, "No License")
    )
    events_solution = models.IntegerField(choices=LICENSES, default=1)
    emarketing_solution = models.IntegerField(choices=LICENSES, default=3)
    suppliers_solution = models.IntegerField(choices=LICENSES, default=3)
    rfps_solution = models.IntegerField(choices=LICENSES, default=3)

    ACCOUNT_NUMBER = 'account_number'

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        name_exist = self.__class__.objects.filter(name=self.name)
        self.account_number = f'{slugify(self.name)[0:5]}00{len(name_exist) + 1}'  # first 5 charechter of name + 001 that goes higher if there is a duplicate of name.
        super().save(*args, **kwargs)
