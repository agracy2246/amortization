import amortization
from amortization import Amortization



am = Amortization(113000.0, .03, 30.0)
print(am.saveReport("testpy.txt"))

print(am.payment)