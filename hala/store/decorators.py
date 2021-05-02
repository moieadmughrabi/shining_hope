
from django.shortcuts import redirect



def notLoggedUsers(view_func):
    def wripper_func(request,*args,**kwargs):

        if request.user.is_authenticated ==False: #if the user author in this website
           return redirect('login')
        else:
           return  view_func(request,*args,**kwargs)
    return wripper_func


def AllowedUsers(AllowedGroups=[]):#get data from views line100
    def decorator(view_func):
        def wripper_func(request,*args,**kwargs):
              group=None
              group=request.user.groups.all()[0].name#there is a problem here
              print(group)
              if request.user.groups.exists():
                  group=request.user.groups.all()[0].name
              if group in  AllowedGroups :
                  return  view_func(request,*args,**kwargs)
              else:
                   return redirect('store_list')  
        return wripper_func        
            
    return decorator




    



    def wripper_func(request,*args,**kwargs):

        if request.user.is_authenticated ==False:
           return redirect('login')
        else:
           return  view_func(request,*args,**kwargs)
    return wripper_func



        
               
            


