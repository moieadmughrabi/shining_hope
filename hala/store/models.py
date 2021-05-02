from django.db import models


class DonationTypes(models.Model):
    DonationType = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.DonationType





class DonersType(models.Model):
    DonersType = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.DonersType


class DonationItemStatus(models.Model):
    DonationItemStatus = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.DonationItemStatus



class RequestDonationStatus(models.Model):
    RequestDonationStatuse = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.RequestDonationStatuse


class Doners(models.Model):
    
    donrName = models.CharField(max_length=100,null=True)
    donrAddress = models.CharField(max_length=150,null=True)
    donrMobile = models.CharField(max_length=20,null=True)
    donrtype = models.ForeignKey(DonersType, null=True,on_delete=models.SET_NULL )
    
    def __str__(self):
        return self.donrName
  
class DonationItems(models.Model):
    ditmType = models.ForeignKey(DonationTypes,  null=True,on_delete=models.SET_NULL )
    ditmDescription = models.CharField(max_length=100,null=True)
    ditmQuantity = models.IntegerField(null=True)
    ditmStatus= models.ForeignKey(DonationItemStatus,  null=True,on_delete=models.SET_NULL )
    ditmimagepath = models.CharField(max_length=200,null=True)
    ditmDoner= models.ForeignKey(Doners,  null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.ditmDescription +' '+ str(self.id)

class RequestDonation(models.Model):# add loged user
    donationItem= models.ForeignKey(DonationItems,  null=True,on_delete=models.SET_NULL )
    RequestDonationStatus= models.ForeignKey(RequestDonationStatus,  null=True,on_delete=models.SET_NULL )
    RequestDonation= models.ForeignKey(Doners,  null=True,on_delete=models.SET_NULL )