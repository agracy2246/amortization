import sys
from django.http import HttpResponse
from django.shortcuts import render


from .amortProcessor import Amortization
from .tablerow       import TableRow

# Create your views here.
def index(request):
    

    if request.method == "GET":
        return render(request, 'app/index.html')    

    elif request.method == "POST":
        
           
        loanAmount = int(request.POST['loanAmount'])
        loanYears  = int(request.POST['loanYears'])
        yearlyInterestDecimal = float(request.POST['yearlyInterestPercent']) / 100.0
        print(type(loanAmount))
        print(type(loanYears))

        am = Amortization(loanAmount, yearlyInterestDecimal, loanYears)
        am.generateSchedule()
        
        
        rowData = []
        loanMonths = am.info['loanYears'] * 12
        for i in range(loanMonths):
            row = TableRow(i+1, am.info['interestList'][i], am.info['principalList'][i], am.info['loanBalanceList'][i])
            rowData.append(row)
        

        data = {
            'loanAmount': am.info['loanAmount'],
            'rowData'   : rowData
        }

        return render(request, 'app/index.html', context=data)
