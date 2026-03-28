from django.urls import path
from.import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('explore', views.explore, name='explore'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('add',views.add,name='add'),
    path('booking/<int:property_id>/',views.booking,name='booking'),
    path('payment/<int:booking_id>/',views.payment,name='payment'),
]



