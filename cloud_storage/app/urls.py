from django.urls import path
from . import views

urlpatterns=[
    path('',views.e_login),
    path('logout',views.e_logout),
    path('user_home',views.user_home),
    path('user_reg',views.user_reg),
    path('delete/<fid>',views.delete_product),
]