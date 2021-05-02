from django.contrib import admin

# Register your models here.
from .models import Doners,DonersType,DonationItems,DonationItemStatus,RequestDonation,RequestDonationStatus,DonationTypes  

admin.site.register(Doners)
admin.site.register(DonersType)

admin.site.register(DonationItems)
admin.site.register(DonationItemStatus)
admin.site.register(DonationTypes)

admin.site.register(RequestDonation)
admin.site.register(RequestDonationStatus)
