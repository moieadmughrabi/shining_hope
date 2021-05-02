from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import *
from .forms import *
from . decorators import unauthenticated_user


def create_department(request):
    if request.method =='POST':
        form=CreateDepartmentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/articles')
    else:
        form = CreateDepartmentform()
        return render(request,'articles/create_department.html',{"form":form})



def article_details(request,emp_id):
    emp=Employee.objects.get(pk=emp_id)
    return render (request,'articles/employee_details.html',{'emps':emp})


def article_delete(request,emp_id):
    emp=Employee.objects.get(pk=emp_id)
    if request.method =='POST':
        emp.delete()
        return redirect('/articles')
    return render (request,'articles/employee_delete.html',{'emp':emp})





def article_list(request):
    emp=Employee.objects.all()
    return render (request,'articles/article_list.html',{'emps':emp})

 
def create_employee(request):
    if request.method =='POST':
        form=CreateDepartmentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/articles')
    else:
        form = CreateEmployeeform()
        return render(request,'articles/create_employee.html',{"form":form})

def edit_employee(request,emp_id):
    emp=Employee.objects.get(pk=emp_id)
    if request.method =='POST':
        form=editemployeeform(request.POST,instance = emp)
        if form.is_valid():
            form.save()
            return redirect('/articles')
    else:
       
        form = editemployeeform(instance = emp)
        return render(request,'articles/update_employee.html',{"form":form})        