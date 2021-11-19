from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Loan(models.Model):
    firstname = models.TextField(max_length=1000,null=True,blank=True)
    lastname = models.TextField(max_length=1000,null=True,blank=True)
    email = models.TextField(max_length=1000,null=True,blank=True)
    phonenumber = models.IntegerField(null=True,blank=True)
    address = models.TextField(max_length=12,null=True,blank=True)
    city = models.TextField(max_length=20,null=True,blank=True)
    state = models.TextField(max_length=20,null=True,blank=True)
    zipcode = models.TextField(max_length=8, null=True,blank=True)
    
    Gender = models.TextField(max_length=1000,null=True,blank=True)
    Married = models.TextField(max_length=1000,null=True,blank=True)
    Dependents = models.IntegerField(blank=True,null=True)
    Education = models.TextField(max_length=1000,null=True,blank=True)
    Self_Employed = models.TextField(max_length=1000,null=True,blank=True)
    ApplicantIncome = models.IntegerField(blank=True,null=True)
    CoapplicantIncome = models.IntegerField(blank=True,null=True)
    LoanAmount = models.IntegerField(blank=True,null=True)
    Loan_Amount_Term = models.IntegerField(blank=True,null=True)
    Credit_History = models.TextField(max_length=1000,null=True,blank=True)
    Property_Area = models.TextField(max_length=1000,null=True,blank=True)
   
class RegistrationForLoan(User):
    
    mobile_no       = models.IntegerField(null=True,blank=True)
    isPremiumMember = models.BooleanField(default=False,null=True,blank=True)
    # premium_amount = models.IntegerField(null=True,blank=True)
    # name_on_card = models.TextField(max_length=50,null=True,blank=True)
    # card_number = models.IntegerField(max_length=20,null=True,blank=True)  
    # card_month = models.TextField(max_length=50,null=True,blank=True)
    # card_year = models.TextField(max_length=50,null=True,blank=True)
    # card_cvv = models.IntegerField(max_length=5,null=True,blank=True)
    
    class Meta:
        Proxy:True

# https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_one/
class PremiumPaymentInfo(models.Model):

    userinfo = models.ForeignKey(RegistrationForLoan, on_delete=models.CASCADE)     
    premium_amount = models.IntegerField(null=True,blank=True)
    name_on_card = models.TextField(max_length=50,null=True,blank=True)
    card_number = models.BigIntegerField(null=True,blank=True)  
    card_month = models.TextField(max_length=50,null=True,blank=True)
    card_year = models.TextField(max_length=50,null=True,blank=True)
    card_cvv = models.IntegerField(null=True,blank=True)
    
    class Meta:
        Proxy:True
        
        
#https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_one/
class RegUserLoanCheckDetails(models.Model):
    
    registeredUser = models.ForeignKey(RegistrationForLoan, on_delete=models.CASCADE)   
    Gender = models.TextField(max_length=10,null=True,blank=True)
    Married = models.TextField(max_length=10,null=True,blank=True)
    Dependents = models.CharField(max_length=3,blank=True,null=True)
    Education = models.TextField(max_length=25,null=True,blank=True)
    Self_Employed = models.TextField(max_length=3,null=True,blank=True)
    ApplicantIncome = models.IntegerField(blank=True,null=True)
    CoapplicantIncome = models.IntegerField(blank=True,null=True)
    LoanAmount = models.IntegerField(blank=True,null=True)
    Loan_Amount_Term_In_Months = models.IntegerField(blank=True,null=True)
    Credit_History = models.TextField(max_length=15,null=True,blank=True)
    Property_Area = models.TextField(max_length=10,null=True,blank=True)
    Result = models.TextField(max_length=15,blank=False,default=False)
    
    class Meta:
        Proxy:True