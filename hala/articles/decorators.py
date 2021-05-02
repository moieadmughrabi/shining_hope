from django.http import HttpResponse
from django.shortcuts import redirect



def unauthenticated_user(view_func):
    def wripper_func(request,*args,**kwargs):

        if request.user.is_authenticated:
           return view_func
           
        else:
            return redirect('../../members/login')
    return wripper_func

        
               
            


