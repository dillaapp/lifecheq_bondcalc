from django.shortcuts import render
from django.http import HttpResponse
from .forms import Bondinfoform
from .models import Bondinfo
from django.contrib.auth.models import User




# Create your views here.













def home(request):
    return render(request,'landingpage.html')

def bondinfo_save(request):
    print(" form is submitted")
    
    Price = int(request.POST["price"])
    Deposit = int(request.POST["deposit"])
    Interest = float(request.POST["R"])
    Loan_term = int(request.POST["term"])


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
    Total_onceoff_payment = Deposit

    Title = "R {0} mortgage with R {1} deposit, {2} % Interest and {3} years loan term"
    Title = Title.format(Loan_amount, Deposit, Interest, Loan_term)
    
   
  


    
    Bond_info = Bondinfo(House_price=Price,Deposit=Deposit, Interest_rate=Interest, Loan_term=Loan_term, Monthly_payment=Monthly_payment, Minimum_monthly_income_required=Minimum_monthly_income_required, Total_interest=Total_interest, Total_onceoff_payment=Total_onceoff_payment, Title=Title)
    Bond_info.save()
          
    


    return render(request, 'result.html',  {
        'Loanamount':Loan_amount,
        'Loanterm': Loan_term, 
        'Deposit': Deposit,
        'Interest': Interest,
        'MonthlyRepayment': Monthly_payment, 
        'MinimumGrossMonthlyIncomeRequired': Minimum_monthly_income_required, 
        'TotalOnceoffCosts': Total_onceoff_payment, 
        'TotalInterest': Total_interest,
        
        

        
        
         })





    
def get(request):
   
    obj= Bondinfo.objects.all().order_by('-Created_at')
    context = {
        
        'objects': obj, 
        }
    return render(request, 'history.html', context)






def backtoregester(request):
    return render(request,'register.html') 

     
   



