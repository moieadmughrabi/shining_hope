from django.db import models

# Create your models here.

class Department (models.Model):
    DName = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.DName

        
class Employee(models.Model):
    cusName = models.CharField(max_length=100,null=True,verbose_name='Customer Name')#0000
    
    cusLastname = models.CharField(max_length=100,null=True)
    cusphone = models.CharField(max_length=100,null=True)
    dep = models.ForeignKey(Department,  null=True,on_delete=models.SET_NULL )
  
    

