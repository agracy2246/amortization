import sys
from django.http import HttpResponse
from django.shortcuts import render

from  import Amortization

# Create your views here.
def index(request):
    am = amortization(120000, .03, 30)
    am.saveReport()
    return render(request, 'app/index.html')
