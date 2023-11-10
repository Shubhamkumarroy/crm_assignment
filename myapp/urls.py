from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('dashboard',views.dashboard,name='dashboard'),
    # path('homepage/',views.homepage,name="homepage"),
    # path('sendmail',views.sendmail,name="sendmail"),
    path('loginuser',views.loginuser,name="loginuser"),
    path('signup',views.signup,name="signup"),
    path('edit/<int:id1>',views.edit,name="edit"),
    path('delete/<int:id1>',views.delete,name="delete"),
    path('addata',views.adddata,name='adddata'),
    path('addcustomer',views.addcustomer,name="addcustomer"),
    path('sendemail/<int:id1>',views.sendemail,name="sendemail"),
    path('logoutuser',views.logoutuser,name="logoutuser"),
    path('chat/<str:receiver_email>', views.chat, name='chat'),
    # path('get_messages/<str:receiver_email>/', views.get_messages, name='get_messages'),
    path('msgdisplay/<str:receiver_email>',views.msgdisplay,name="msgdisplay")


   
]