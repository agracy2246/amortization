
import io

class Amortization():
    # the initial loan amount
    loanAmount          = 0.0
    # yearly interest rate passed in as a decimal
    yearlyInterestRate  = 0.0
    # balance after a payment
    loanBalance         = 0.0
    # payment term
    term                = 0.0
    # monthly payment
    payment             = 0.0
    # duration of loan in years
    loanYears           = 0.0
    # list holds info about payments
    info                = {}
    principalList       = []
    interestList        = []
    loanBalanceList     = []


    def __init__(self, loanAmount, yearlyInterestRate, loanYears):
        self.loanAmount             = loanAmount
        self.loanBalance            = loanAmount
        self.yearlyInterestRate     = yearlyInterestRate
        self.loanYears              = loanYears
        self.info["loanAmount"]     = loanAmount
        self.info["rate"]           = yearlyInterestRate
        self.info["loanYears"]      = loanYears
        self.info["principalList"]  = self.principalList
        self.info["interestList"]   = self.interestList
        self.info["loanBalanceList"]= self.loanBalanceList
        self.calcPayment()
        
    
    def calcPayment(self):
        self.term = float((1.0 + self.yearlyInterestRate / 12.0)**(12.0 * self.loanYears))
        self.payment = (self.loanAmount * self.yearlyInterestRate / 12.0 * self.term ) / (self.term - 1)
        

    def getNumberOfPayments(self):
        return 12 * int(self.loanYears)

    def saveReport(self, filename):
        file = open(filename, 'w')

        file.write("Monthly Payment: %s\n" % str(round(self.payment,2)))
        
        for i in range(self.getNumberOfPayments()):
            monthlyInterest = self.yearlyInterestRate / 12.0 * self.loanBalance
            self.info["interestList"].append(round(monthlyInterest,2))
            
            if i != self.getNumberOfPayments() - 1.0:
                principal = self.payment - monthlyInterest
                self.info["principalList"].append(round(principal,2))    
            else:
                principal = self.loanBalance
                self.info["principalList"].append(round(principal,2))
                self.payment = self.loanBalance + monthlyInterest
            
            self.loanBalance -= principal
            self.info["loanBalanceList"].append(round(self.loanBalance,2))

            file.write("Month %d:      Principal = %s,       Interest = %s,       Loan Balance: %s\n" % (i+1, str(round(principal,2)), str(round(monthlyInterest,2)), str(round(self.loanBalance,2))))
        
        
if __name__ == '__main__':
    print('Mod2 UnitTest!')