from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path

from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('store/', include('store.urls')),

    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),

    path('home/', views.homepage),

]
