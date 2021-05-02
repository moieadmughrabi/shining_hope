from django.contrib import admin
from django.urls import path

from.import views

urlpatterns = [
    
    path('', views.article_list,name='employee_list'),
    path('create_employee/', views.create_employee,name='employee_create'),
    path('edit_employee/<int:emp_id>', views.edit_employee,name='employee_update'),
    path('article_details/<int:emp_id>',views.article_details,name='employee_details'),
    path('article_delete/<int:emp_id>',views.article_delete,name='employee_delete'),
    path('create_department/', views.create_department,name='department_create'),
]

