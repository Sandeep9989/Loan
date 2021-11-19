from django.contrib import admin

# Register your models here.
from .models import *
# class LoanAdmin(admin.ModelAdmin):
#     pass

# mobile_no       = models.IntegerField(null=True,blank=True)
# isPremiumMember = models.BooleanField(default=False,null=True,blank=True)

class Admin_RegistrationForLoan(admin.ModelAdmin):

    list_display = ['first_name','last_name','username','email','mobile_no','isPremiumMember']
    list_filter = ['first_name','last_name','isPremiumMember']
    search_fields = ['first_name','last_name','isPremiumMember']
    list_display_links = ['username', 'last_name']
    
    class meta:
        model = RegistrationForLoan


class Admin_RegUserLoanCheckDetails(admin.ModelAdmin):
    
    list_display = ['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term_In_Months','Credit_History','Property_Area','Result']
    list_filter =  ['Gender','Married','Dependents','CoapplicantIncome','LoanAmount','Loan_Amount_Term_In_Months','Result']
    list_search =  ['Gender','Married','Dependents','CoapplicantIncome','LoanAmount','Loan_Amount_Term_In_Months','Result']
    list_display_links = ['Gender','Married']
    
    class meta:
        model = RegUserLoanCheckDetails

class Admin_PremiumPaymentInfo(admin.ModelAdmin):
    
    list_display = ['userinfo','name_on_card','card_number','card_month','card_year','card_cvv','premium_amount']
    list_filter = ['name_on_card','card_year']
    search_fields = ['name_on_card','card_year']
    list_display_links = ['userinfo','name_on_card', 'card_number']
    
    class meta:
        model = PremiumPaymentInfo



# registeredUser = models.ForeignKey(RegistrationForLoan, on_delete=models.CASCADE)   
    
admin.site.register(Loan)
admin.site.register(RegistrationForLoan,Admin_RegistrationForLoan)
admin.site.register(RegUserLoanCheckDetails,Admin_RegUserLoanCheckDetails)
admin.site.register(PremiumPaymentInfo,Admin_PremiumPaymentInfo)

