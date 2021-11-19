from django.shortcuts import render
from LoanProcessingApp.models import Loan
from .models import * 
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist
from win32.lib.winxptheme import IsAppThemed

def data(request):
    return render(request,'html/form.html')

def header(request):
    return render(request,'html/header.html')

def userregistration(request):
    if request.method == 'POST':
        firstname   =   request.POST.get('first_name')
        lastname    =   request.POST.get('last_name')
        username    =   request.POST.get('username')
        email       =   request.POST.get('email')
        phonenumber =   request.POST.get('phonenumber')
        password    =   request.POST.get('password')
        confirm_password =request.POST.get('confirm_password')
        
        Premium_Membership =    request.POST.get('Premium_Membership')
        name_on_card       =    request.POST.get('name_on_card')
        card_number        =    request.POST.get('card_number')
        card_month         =    request.POST.get('card_month')
        card_year          =    request.POST.get('card_year')
        card_cvv           =    request.POST.get('card_cvv')
        
        print(Premium_Membership,name_on_card,card_number,card_month,card_year,card_cvv)


        if password != confirm_password:
            context={'outputmessage':'Password and confirm password did not match',
            'first_name':firstname,
            'last_name':lastname,
            'username':username,
            'email':email,
            'mobileno':phonenumber}
            return render(request,'html/userregistration.html',context)

        alreadythere = False
        try:
            RegistrationForLoan.objects.get(email=email)
            alreadythere = True
            context={'outputmessage':'with same details(email) user is already there',
            'first_name':firstname,
            'last_name':lastname,
            'username':username,
            'email':email,
            'mobileno':phonenumber}
            return render(request,'html/userregistration.html',context)
        except ObjectDoesNotExist:
            alreadythere = False

        if alreadythere is False:
            reg = RegistrationForLoan.objects.create(first_name=firstname,
            last_name=lastname,
            username=username,
            email=email,
            password=make_password(password),
            mobile_no=phonenumber)
            reg.save()
            print("after saving the user")
            if Premium_Membership :
                print("premium member")
                reg.isPremiumMember = True
                reg.save()
                
                PremiumPaymentInfo.objects.create(
                userinfo = reg,
                premium_amount = 10,
                name_on_card = name_on_card,
                card_number =card_number,
                card_month = card_month,
                card_year = card_year,
                card_cvv = card_cvv).save()
                
            
            context={'outputmessage':'Your account got created',}
            
            return render(request,'html/userregistration.html',context)
    
    return render(request,'html/userregistration.html')






def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        mobilenumber = request.POST.get('mobilenumber')
        password = request.POST.get('password')
        
        try:
            reguser = RegistrationForLoan.objects.get(email=email,mobile_no=mobilenumber)
        except ObjectDoesNotExist:
            context={
                'authentication_message':'No User Found with given details',
                'email':email,
                'mobilenumber':mobilenumber
            }
            return render(request,'html/signin.html',context)

        check_password_work = check_password(password, reguser.password)

        if check_password_work:
            
            user_authenticate = authenticate(username = reguser.username, password=password)
            login(request,user_authenticate)
            context={
                'authentication_message':'successfully authenticated'
            }
            return render(request,'html/Reg_User_LoanCheck.html',context)
            
        else:
            context={
                'authentication_message':'you entered wrong password',
                'email':email,
                'mobilenumber':mobilenumber
            }
            return render(request,'html/signin.html',context)

    
    return render(request,'html/signin.html')

def reg_user_logout(request):

    logout(request)
    return render(request,'html/signin.html')

def reg_user_loan_check(request):
    
    return render(request,'html/Reg_User_LoanCheck.html')

# def registering_user_loan_check(request):
#     print("this is from registering_user_loan_check")
#     return render(request,'html/Reg_User_LoanCheck.html')

def reg_User_Loan_Check_History(request):
    
    reguser = RegistrationForLoan.objects.get(email=request.user.email)
    
   
    loanCheckeddetailsList = RegUserLoanCheckDetails.objects.filter(registeredUser=reguser)
    
    context={'loanCheckeddetailsList':loanCheckeddetailsList}
    
    return render(request, 'html/Reg_User_Loan_Check_History.html',context)

def submitdata(request):
    print("this is from submit data")   
    firstname =request.POST.get('firstname')
    lastname =request.POST.get('lastname')
    phonenumber=request.POST.get('phonenumber')
    email =request.POST.get('email')
    address=request.POST.get('address')
    city=request.POST.get('city')
    state=request.POST.get('state')
    zipcode=request.POST.get('zipcode')
    Gender =request.POST.get('gender')
    Married =request.POST.get('maritalstatus')
    Dependents=request.POST.get('dependents')
    Education =request.POST.get('education')
    Self_Employed=request.POST.get('SelfEmployed')
    ApplicantIncome =request.POST.get('ApplicantIncome')
    CoapplicantIncome=request.POST.get('CoapplicantIncome')
    LoanAmount =request.POST.get('LoanAmount')
    Loan_Amount_Term =request.POST.get('LoanAmountTerm')
    Credit_History=request.POST.get('credithistory')
    Property_Area=request.POST.get('Propertyarea')
    
    # Index(['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
    #    'Loan_Amount_Term', 'Credit_History', 'Gender_Male', 'Married_Yes',
    #    'Dependents_1', 'Dependents_2', 'Dependents_3', 'Dependents_3+',
    #    'Education_Not_Graduate', 'Self_Employed_Yes',
    #    'Property_Area_Semiurban', 'Property_Area_Urban'],
    
    
    loan = Loan(
        firstname= firstname,lastname = lastname,email = email,
        phonenumber = phonenumber,address = address,city = city,state = state,zipcode = zipcode,
        Gender=Gender,Married=Married,Dependents=Dependents,Education=Education,Self_Employed=Self_Employed,
        ApplicantIncome=ApplicantIncome,CoapplicantIncome=CoapplicantIncome,LoanAmount=LoanAmount,
        Loan_Amount_Term=Loan_Amount_Term,Credit_History=Credit_History,Property_Area=Property_Area
    )
    loan.save()
    
    
    return render(request,'html/output.html')

import joblib

def reg_user_loancheck(request):
    print("this is from reg_user_loancheck")   
  
    Gender =request.POST.get('gender')
    Married = request.POST.get('maritalstatus')
    Dependents=request.POST.get('dependents')
    Education =request.POST.get('education')
    Self_Employed=request.POST.get('SelfEmployed')
    ApplicantIncome =request.POST.get('ApplicantIncome')
    CoapplicantIncome=request.POST.get('CoapplicantIncome')
    LoanAmount =request.POST.get('LoanAmount')
    Loan_Amount_Term =request.POST.get('LoanAmountTerm')
    credithistory=request.POST.get('credithistory')
    Property_Area=request.POST.get('Propertyarea')
       
    print(Dependents)
    # print(Dependents.type())
    
    if Married == "Married":
        Married_Yes = 1
    else:
        Married_Yes = 0
    
    if credithistory == 'good':
        Credit_History = 1
    else:
        Credit_History = 0
        
    if Gender=='male':
        Gender_Male = 1
    else: 
        Gender_Male = 0
     
    if Dependents == '1':
        Dependents_1 = 1
        Dependents_2 = 0
        Dependents_3 = 0
        Dependents_moreth3 = 0
    
    if Dependents == '2':
        Dependents_1 = 0
        Dependents_2 = 1
        Dependents_3 = 0
        Dependents_moreth3 = 0
    
    if Dependents == '3':
        Dependents_1 = 0
        Dependents_2 = 0
        Dependents_3 = 1
        Dependents_moreth3 = 0
        
    if Dependents == '3+':
        Dependents_1 = 0
        Dependents_2 = 0
        Dependents_3 = 0
        Dependents_moreth3 = 1
        
    if Education =='lower' or Education =='high':
        
        Education_Not_Graduate = 1
    else:
        Education_Not_Graduate = 0
    
    if Self_Employed == 'yes':
        
        Self_Employed_Yes = 1
    else:
        Self_Employed_Yes = 0
    
    if Property_Area == 'Urban':
        Property_Area_Urban = 1
        Property_Area_Semiurban = 0
    
    if Property_Area == 'Rural':
        Property_Area_Urban = 0
        Property_Area_Semiurban = 0
    
    if Property_Area == 'semiurban':
        Property_Area_Urban = 0
        Property_Area_Semiurban = 1 
    

    loan_parameters_list = []
    loan_parameters_list.append(ApplicantIncome)
    loan_parameters_list.append(CoapplicantIncome)
    loan_parameters_list.append(LoanAmount)
    loan_parameters_list.append(Loan_Amount_Term)
    loan_parameters_list.append(Credit_History)
    loan_parameters_list.append(Gender_Male)
    loan_parameters_list.append(Married_Yes)
    loan_parameters_list.append(Dependents_1)
    loan_parameters_list.append(Dependents_2)
    loan_parameters_list.append(Dependents_3)
    loan_parameters_list.append(Dependents_moreth3)
    loan_parameters_list.append(Education_Not_Graduate)
    loan_parameters_list.append(Self_Employed_Yes)
    loan_parameters_list.append(Property_Area_Semiurban)
    loan_parameters_list.append(Property_Area_Urban)
    
    # Index(['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
    #    'Loan_Amount_Term', 'Credit_History', 'Gender_Male', 'Married_Yes',
    #    'Dependents_1', 'Dependents_2', 'Dependents_3', 'Dependents_moreth3',
    #    'Education_Not_Graduate', 'Self_Employed_Yes',
    #    'Property_Area_Semiurban', 'Property_Area_Urban'],
    #   dtype='object')
    
    loanModel = joblib.load("LoanApproval.sav")
    isApproved = loanModel.predict([loan_parameters_list])
    reguser = RegistrationForLoan.objects.get(email=request.user.email)
    message=''
    if isApproved[0] == 1:
        message='approve'
    elif isApproved[0] == 0:
        message='not approve'

    regUserLoanCheckDetails = RegUserLoanCheckDetails.objects.create(registeredUser=reguser,
                            Gender=Gender,Married=Married,
                            Dependents=Dependents,Education=Education,
                            Self_Employed=Self_Employed,ApplicantIncome=ApplicantIncome,
                            CoapplicantIncome=CoapplicantIncome,LoanAmount=LoanAmount,
                            Loan_Amount_Term_In_Months=Loan_Amount_Term,Credit_History=credithistory,
                            Property_Area=Property_Area,Result = message
                            )
    regUserLoanCheckDetails.save()
    
    if reguser.isPremiumMember:
        sendEmailWithLoanDetails(regUserLoanCheckDetails)

    if isApproved[0] == 1:
         
        return render(request,'html/Reg_User_LoanCheck.html',{'loanapproved_info':
        'For the provided information, your loan gets approve'})
    elif isApproved[0] == 0:
         
        return render(request,'html/Reg_User_LoanCheck.html',{'loanapproved_info':
        'For the provided information, your loan does not get approve'})
         
    
    return render(request,'html/output.html')

def processloandetails(request):
    
    if request.method == 'POST':
        
    
        Gender =request.POST.get('gender')
        Married = request.POST.get('maritalstatus')
        Dependents=request.POST.get('dependents')
        Education =request.POST.get('education')
        Self_Employed=request.POST.get('SelfEmployed')
        ApplicantIncome =request.POST.get('ApplicantIncome')
        CoapplicantIncome=request.POST.get('CoapplicantIncome')
        LoanAmount =request.POST.get('LoanAmount')
        Loan_Amount_Term =request.POST.get('LoanAmountTerm')
        credithistory=request.POST.get('credithistory')
        Property_Area=request.POST.get('Propertyarea')
           
        print(Dependents)
        # print(Dependents.type())
        
        if Married == "Married":
            Married_Yes = 1
        else:
            Married_Yes = 0
        
        if credithistory == 'good':
            Credit_History = 1
        else:
            Credit_History = 0
            
        if Gender=='male':
            Gender_Male = 1
        else: 
            Gender_Male = 0
         
        if Dependents == '1':
            Dependents_1 = 1
            Dependents_2 = 0
            Dependents_3 = 0
            Dependents_moreth3 = 0
        
        if Dependents == '2':
            Dependents_1 = 0
            Dependents_2 = 1
            Dependents_3 = 0
            Dependents_moreth3 = 0
        
        if Dependents == '3':
            Dependents_1 = 0
            Dependents_2 = 0
            Dependents_3 = 1
            Dependents_moreth3 = 0
            
        if Dependents == '3+':
            Dependents_1 = 0
            Dependents_2 = 0
            Dependents_3 = 0
            Dependents_moreth3 = 1
            
        if Education =='lower' or Education =='high':
            
            Education_Not_Graduate = 1
        else:
            Education_Not_Graduate = 0
        
        if Self_Employed == 'yes':
            
            Self_Employed_Yes = 1
        else:
            Self_Employed_Yes = 0
        
        if Property_Area == 'Urban':
            Property_Area_Urban = 1
            Property_Area_Semiurban = 0
        
        if Property_Area == 'Rural':
            Property_Area_Urban = 0
            Property_Area_Semiurban = 0
        
        if Property_Area == 'semiurban':
            Property_Area_Urban = 0
            Property_Area_Semiurban = 1 
        
    
        loan_parameters_list = []
        loan_parameters_list.append(ApplicantIncome)
        loan_parameters_list.append(CoapplicantIncome)
        loan_parameters_list.append(LoanAmount)
        loan_parameters_list.append(Loan_Amount_Term)
        loan_parameters_list.append(Credit_History)
        loan_parameters_list.append(Gender_Male)
        loan_parameters_list.append(Married_Yes)
        loan_parameters_list.append(Dependents_1)
        loan_parameters_list.append(Dependents_2)
        loan_parameters_list.append(Dependents_3)
        loan_parameters_list.append(Dependents_moreth3)
        loan_parameters_list.append(Education_Not_Graduate)
        loan_parameters_list.append(Self_Employed_Yes)
        loan_parameters_list.append(Property_Area_Semiurban)
        loan_parameters_list.append(Property_Area_Urban)
        
        # Index(['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
        #    'Loan_Amount_Term', 'Credit_History', 'Gender_Male', 'Married_Yes',
        #    'Dependents_1', 'Dependents_2', 'Dependents_3', 'Dependents_moreth3',
        #    'Education_Not_Graduate', 'Self_Employed_Yes',
        #    'Property_Area_Semiurban', 'Property_Area_Urban'],
        #   dtype='object')
    
        loanModel = joblib.load("LoanApproval.sav")
        
        isApproved = loanModel.predict([loan_parameters_list])
        print(" results ")
        
        print(isApproved[0])
        if isApproved[0] == 1:
             # return render(request,'html/output.html')
            return render(request,'html/LoanDetails.html',{'loanapproved_info':'For the provided information, your loan gets approve'})
        elif isApproved[0] == 0:
             # return render(request,'html/output.html')
            return render(request,'html/LoanDetails.html',{'loanapproved_info':'For the provided information, your loan does not get approve'})
    
    return render(request,'html/LoanDetails.html')

from django.conf import settings 
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core import mail

def sendEmailWithLoanDetails(regUserLoanCheckDetails):
    
    sub_line = 'Loan Details :'
    
    text = render_to_string('html/LoanCheckDetailsEmail.html', {'regUserLoanCheckDetails': regUserLoanCheckDetails})
    
    message = strip_tags(text)
    
    email_from = settings.EMAIL_HOST_USER  
    
    recipient_list = [regUserLoanCheckDetails.registeredUser.email,'loanchecking123@gmail.com']
    
    mail.send_mail(sub_line, message, email_from, recipient_list, html_message=text)
    
    
    