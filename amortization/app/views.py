import sys
from django.http import HttpResponse
from django.shortcuts import render


from .amortProcessor import Amortization
from .tablerow       import TableRow

# Create your views here.
def index(request):
    am = Amortization(250000, .02, 30)
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
