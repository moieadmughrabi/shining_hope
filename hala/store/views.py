from django.shortcuts import render,redirect
from django.contrib import auth
from django.http import HttpRequest
from .models import Doners,DonationItems,RequestDonation,DonationItemStatus,RequestDonationStatus
from .models import *
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage
from .forms import *

from .decorators import notLoggedUsers,AllowedUsers
# Create your views here.






@notLoggedUsers

@AllowedUsers(AllowedGroups=['admin'])
def requestDonation_list(request):
    items=RequestDonation.objects.all()#problem here
    return render (request,'store/requestDonation_list.html',{'items':items})




'''--------------------------------'''


def store_list(request):

    if request.method =='POST':
        #get item
        pid=request.POST.get('itm')
        don_item =DonationItems.objects.get(id=pid)

        don_itm_st_id= DonationItemStatus.objects.get(DonationItemStatus=don_item.ditmStatus)
        don_item_obj=DonationItems.objects.get(id=pid)
        if request.user.is_authenticated ==False:
            return redirect('login')
        else:
            if don_item_obj.ditmQuantity >0: 
                obj=RequestDonation.objects.create()
                obj.donationItem=don_item
                obj.RequestDonationStatus=RequestDonationStatus.objects.get(id=1)#حالة الطلب
                obj.RequestDonation=don_item.ditmDoner #   
                obj.save()
                
                don_item_obj.ditmQuantity =don_item_obj.ditmQuantity-1
                if don_item_obj.ditmQuantity <=0:
                    don_item_obj.ditmStatus= DonationItemStatus.objects.get(id=0)
                don_item_obj.save()
            
    
    items=DonationItems.objects.all()
   
    Dt=DonationTypes.objects.all()
    return render (request,'store/store_list.html',{'items':items,'Dt':Dt})

'''--------------------------------'''
@notLoggedUsers
@AllowedUsers(AllowedGroups=['admin'])#edit later
def donationItems_list(request):
    items=DonationItems.objects.all()
    paginator=Paginator(items,6)#how many items viewed in one page
    page_number=request.GET.get('page',1)  
    item_obj=paginator.page(page_number)
    context= {
        'items':item_obj
    }   
    return render (request,'store/donationItems_list.html',context)
@notLoggedUsers
@AllowedUsers(AllowedGroups=['admin'])
def donationItems_details(request,DonationItems_id):
    item=DonationItems.objects.get(pk=DonationItems_id)
    return render (request,'store/donationItems_details.html',{'items':item})

@notLoggedUsers
@AllowedUsers(AllowedGroups=['admin'])#check this to add permisson to create 
def donationItems_create(request):
    if request.method =='POST':
        form=CreateDonationItemsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/store/donationItems_list')
    else:
        form = CreateDonationItemsForm()
        return render(request,'store/donationItems_create.html',{"form":form})
@notLoggedUsers
@AllowedUsers(AllowedGroups=['admin'])
def donationItems_edit(request,DonationItems_id):
    obj=DonationItems.objects.get(pk=DonationItems_id)
    if request.method =='POST':
        form=EditDonationItemsForm(request.POST,instance = obj)
        if form.is_valid():
            form.save()
            return redirect('/store/donationItems_list')
    else:
       
        form = EditDonationItemsForm(instance = obj)
        return render(request,'store/donationItems_edit.html',{"form":form})  
@notLoggedUsers
@AllowedUsers(AllowedGroups=['admin'])
def donationItems_delete(request,DonationItems_id):
    item=DonationItems.objects.get(pk=DonationItems_id)
    if request.method =='POST':
        item.delete()
        return redirect('/store/')
    return render (request,'store/donationItems_delete.html',{'item':item})


'''--------------------------------'''
@notLoggedUsers
@AllowedUsers(AllowedGroups=['admin'])
def doner_list(request):
    items=Doners.objects.all()
    return render (request,'store/doner_list.html',{'items':items})

@notLoggedUsers
@AllowedUsers(AllowedGroups=['admin'])
def doner_details(request,doner_id):
    items=Doners.objects.get(pk=doner_id)
    return render (request,'store/doner_details.html',{'items':items})
@notLoggedUsers
@AllowedUsers(AllowedGroups=['admin'])
def doner_create(request):
    if request.method =='POST':
        form=CreateDonersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/store/doner_list')
    else:
        form = CreateDonersForm()
        return render(request,'store/doner_create.html',{"form":form})

@notLoggedUsers
@AllowedUsers(AllowedGroups=['admin'])
def doner_edit(request,doner_id):
    emp=Doners.objects.get(pk=doner_id)
    if request.method =='POST':
        form=EditDonersform(request.POST,instance = emp)
        if form.is_valid():
            form.save()
            return redirect('/store/doner_list')
    else:
       
        form = EditDonersform(instance = emp)
        return render(request,'store/doner_edit.html',{"form":form})        
@notLoggedUsers
@AllowedUsers(AllowedGroups=['admin'])
def doner_delete(request,doner_id):
    emp=Doners.objects.get(pk=doner_id)
    if request.method =='POST':
        emp.delete()
        return redirect('/store/doner_list')
    return render (request,'store/doner_delete.html',{'emp':emp})



def TagSearch(request):
   Dt=DonationItems.objects.all()
    
   return render(request,'search.html',{'Dt':Dt})
   
 