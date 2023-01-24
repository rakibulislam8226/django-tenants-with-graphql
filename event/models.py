from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone
from django_tenants.models import TenantMixin, DomainMixin
from client.models import Client


# Create your models here.
class EventDomain(DomainMixin):
    pass


class Event(TenantMixin):
    client = models.ForeignKey(Client, related_name='events', blank=True, null=True, on_delete=models.PROTECT)  # client name
    is_active = models.BooleanField(default=True, blank=True, null=True)  # Is the event active?
    published = models.BooleanField(default=False)  # has the event been published
    redirected = models.BooleanField(default=False)  # has the event been redirected to showsite
    created_on = models.DateField(auto_now_add=True)  # the date the event was created
    event_name = models.CharField(max_length=255)  # Name of Event
    event_description = models.TextField(max_length=None, blank=True, null=True)
    launched = models.DateTimeField(default=timezone.now, null=True, blank=True)  # date and time event was launched
    registration_deadline = models.DateTimeField(default=timezone.now, null=True, blank=True)
    event_start = models.DateTimeField(default=timezone.now, null=True, blank=True)
    event_end = models.DateTimeField(default=timezone.now, null=True, blank=True)
    archive_date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    event_code = models.CharField(max_length=11, null=True,  blank=True)
    EVENT_STATUS_CHOICE = (
        ("A", "Active"),
        ("P", "Pending"),
        ("C", "Completed"),
    )
    event_status = models.CharField(max_length=1, choices=EVENT_STATUS_CHOICE, default="P")  # Event choices to organize events based on progress
    EVENT_TYPE_CHOICE = (
        ("R", "Registration"),
        ("P", "Presentation Management"),
        ("M", "Registration + Presentation Management"),
    )
    event_type = models.CharField(max_length=1, choices=EVENT_TYPE_CHOICE, default="R")  # Type of event technology used
    EVENT_CATEGORY = (
        ("1", "Conference"),
        ("2", "Meeting"),
        ("3", "Seminar"),
        ("4", "Training Session"),
        ("5", "Trade Show"),
        ("6", "Webinar"),
        ("7", "Incentive Trip"),
        ("8", "Other / General"),
        ("9", "Sport Event"),
        ("10", "Reunion"),
        ("11", "Holiday"),
        ("12", "Celebration"),
        ("13", "Save The Date"),
        ("14", "Fundraiser / Benefit"),
        ("15", "Forum"),
        ("16", "Political Event"),
        ("17", "Dinner"),
    )
    event_category = models.CharField(max_length=2, choices=EVENT_CATEGORY, default="8")  # Type of event
    internal_note = models.TextField(max_length=300, blank=True, null=True)  # Internal Note
    language = models.CharField(max_length=30, blank=True, null=True)  # Language the event website
    capacity = models.IntegerField(null=True, blank=True)
    keywords = models.CharField(max_length=255, blank=True, null=True)  # Examples: AES, online registration, event management
    event_passcode = models.CharField(max_length=255, blank=True, null=True)
    display_policy = models.BooleanField(default=False)
    cookie_notification = models.BooleanField(default=False)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True
    domain_name = models.CharField(max_length=253, null=True, blank=True)

    # def __str__(self):
    #     return self.event_name
    def __str__(self):
        if self.event_name:
            return self.event_name
        else:
            return self.id


# create domain for an event
@receiver(post_save, sender=Event)
def create_event_domain(sender, instance, created, **kwargs):
    if created:
        event_domain = EventDomain()
        # set Tenant instance
        event_domain.tenant = instance
        # set Tenant domain name like demo.dsi.com
        domain_name = str(instance.schema_name).lower().strip() + "." + settings.HOST_DOMAIN_NAME
        event_domain.domain = domain_name
        event_domain.is_primary = True
        # create domain for a tenant
        event_domain.save()

        # set event domain_name
        instance.domain_name = domain_name
        instance.save()
