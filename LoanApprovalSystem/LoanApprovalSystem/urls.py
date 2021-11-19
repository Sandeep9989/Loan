"""LoanApprovalSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from LoanProcessingApp import views
from django.conf.urls import url

urlpatterns = [
    
    path('admin/', admin.site.urls),
    url("^$", views.signin, name="signin"),
    path("submit", views.data, name="submit"),
    path("loancheck_for_registered_user", views.reg_user_loancheck, name="reg_user_loancheck"),
    path("loancheck-know-by-yourself", views.processloandetails, name="loandetails"),
    path("header", views.header, name="header"),
    path("user_registration", views.userregistration, name="userregistrtion"),
    path("sign-in-registered-users", views.signin, name="signin"),
    path("registered_user_loan_checking", views.reg_user_loan_check, name="reg_user_loan_check"),
    path("registered_user_loan_history", views.reg_User_Loan_Check_History, name="reg_User_Loan_Check_History"),
    path("sign-out-registered-users", views.reg_user_logout, name="signout"),
      
]
