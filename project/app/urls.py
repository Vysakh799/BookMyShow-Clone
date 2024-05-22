from django.urls import path
from .import views

urlpatterns=[
    path('login',views.login),
    path('logout',views.logout1),
    path('',views.index),
    path("see_all",views.see_all),
    path("movie/<name>",views.view_movie),
    path('register',views.register),
]