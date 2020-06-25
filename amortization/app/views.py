import sys
from django.http import HttpResponse
from django.shortcuts import render


from .amortProcessor import Amortization


# Create your views here.
def index(request):
    am = Amortization(120000, .03, 30)
    am.generateSchedule()
    
    data = am.info

    data = {
        'loanAmount': am.info['loanAmount'],

    }
    return render(request, 'app/index.html', context=am.info)
