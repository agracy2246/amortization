import amortization
from amortization import Amortization



am = Amortization(129290.0, .03, 15.0)

print(am.saveReport("testpy.txt"))
print(am.info.get("rate"))
