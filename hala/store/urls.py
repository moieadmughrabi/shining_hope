from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [

    path('', views.store_list,name='store_list'),

    path('requestDonation_list/', views.requestDonation_list,name='requestDonation_list'),

    path('doner_list/', views.doner_list,name='doner_list'),
    path('doner_create/', views.doner_create,name='create_doner'),
    path('doner_edit/<int:doner_id>', views.doner_edit,name='edit_doner'),
    path('doner_delete/<int:doner_id>', views.doner_delete,name='delete_doner'),
    path('doner_details/<int:doner_id>', views.doner_details,name='details_doner'),

    path('donationItems_list/', views.donationItems_list,name='list_donationItems'),
    path('DonationItems_details/<int:DonationItems_id>', views.donationItems_details,name='details_DonationItems'),
    path('donationItems_deletedelete/<int:DonationItems_id>', views.donationItems_delete,name='delete_donationItems'),
    path('donationItem_create/', views.donationItems_create,name='create_donationItems'),
    path('donationItems_edit/<int:DonationItems_id>', views.donationItems_edit,name='edit_donationItems'),
    
    path('search/',views.TagSearch,name='search')
]

