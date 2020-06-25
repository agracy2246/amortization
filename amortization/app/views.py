import sys
from django.http import HttpResponse
from django.shortcuts import render


from .amortProcessor import Amortization


# Create your views here.
def index(request):
    am = Amortization(120000, .03, 30)
    am.generateSchedule()
    
    data = am.info
    # need to build a row for each month consisting of Month, interest, principal
    # a list of dictionaries

    loanMonths = data['loanYears'] * 12
    print(loanMonths)

    data = {
        'loanAmount': am.info['loanAmount'],

    }
    return render(request, 'app/index.html', context=am.info)
