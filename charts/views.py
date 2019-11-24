from django.shortcuts import render
from django.http import HttpResponse
from calc.models import Bondinfo



# Create your views here.

def getdata(request):
   
    
    ## input
    Price = 100000#Bondinfo.objects.House_price 
    Deposit = 1000#Bondinfo.objects.Deposit
    Interest =8 #Bondinfo.objects.Interest_rate
    Loan_term = 5#Bondinfo.objects.Loan_term
    

    ## calculations for output
    Loan_amount = Price - Deposit
    Monthly_interest = (Interest / 12) / 100
    Number_of_months = Loan_term * 12
    x = Monthly_interest *  Loan_amount
    y = 1 - (1 + Monthly_interest) ** (-1 * Number_of_months)
  
   
   ## output for results page
  
    Monthly_payment = int(x / y)
    Total_interest = int((Monthly_payment * Number_of_months) - Loan_amount)
    Minimum_monthly_income_required = int(Monthly_payment / 0.28)
    Total_onceoff_payment = int(Deposit)

    
   ## output for charts 
    

    Interest_rate = []

    Principal_rate = []

    Interest_payment = []

    principal_payment =[] 

    Yearly_payment = []

    Total_Balance =[]




    for i in range(1, Loan_term +1):   
        
        
        
        Scheduled_yearly_payment = float(Monthly_payment * 12)

        Yearly_interest_paid = float(((Interest/100) * Loan_amount))
        Yearly_Principal_paid = float(Scheduled_yearly_payment - Yearly_interest_paid)
        Loan_amount = Loan_amount - float(Yearly_Principal_paid)
        

        

        Yearly_interestrate = (Yearly_interest_paid / Scheduled_yearly_payment) * 100
       
        Yearly_Principalrate = (Yearly_Principal_paid / Scheduled_yearly_payment) * 100
        


        

       
        Interest_rate.append(Yearly_interestrate)
        Principal_rate.append(Yearly_Principalrate)
        Interest_payment.append(Yearly_interest_paid)
        principal_payment.append(Yearly_Principal_paid) 
        Yearly_payment.append(Scheduled_yearly_payment)
        Total_Balance.append(Loan_amount )


    

    
    
    
    
    context = {
        
        #'objects': obj, 
        'Interestrate': Interest_rate,
        'Principalrate': Principal_rate,
        'Loanterm': Loan_term,
        'Loanterm': Loan_term, 
        'Deposit': Deposit,
        'Interestpayment': Interest_payment,
        'Principalpayment': principal_payment,
        'Yearlypayment': Yearly_payment, 
        'Totalbalance': Total_Balance,
        'Interest': Interest, 

        }
    return render(request, 'chart.html', context)

    
    

    




 





