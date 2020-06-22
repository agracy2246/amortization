# c is the monly payment, which depends on:

# r the monthly interest rate (as a decimal).
# it is yearly percentage / 12 / 100

# N is the number of monthly payments, called loans term

# P is the principal
import io

class Amortization():
    loanAmount          = 0.0
    yearlyInterestRate  = 0.0
    loanBalance         = 0.0
    term                = 0.0
    payment             = 0.0
    loanYears           = 0.0
    info                = {}


    def __init__(self, loanAmount, yearlyInterestRate, loanYears):
        self.loanAmount         = loanAmount
        self.loanBalance        = loanAmount
        self.yearlyInterestRate = yearlyInterestRate
        self.loanYears          = loanYears
        self.info["loanAmount"] = loanAmount
        self.info["rate"]       = yearlyInterestRate
        self.calcPayment()
        
    
    def calcPayment(self):
        self.term = float((1.0 + self.yearlyInterestRate / 12.0)**(12.0 * self.loanYears))

        self.payment = float((self.loanAmount * self.yearlyInterestRate / 12.0 * self.term ) / (self.term - 1))
        

    def getNumberOfPayments(self):
        return 12 * int(self.loanYears)

    def saveReport(self, filename):
        file = open(filename, 'w')

        file.write("Monthly Payment: %s\n" % str(round(self.payment,2)))
        
        for i in range(self.getNumberOfPayments()):
            monthlyInterest = self.yearlyInterestRate / 12.0 * self.loanBalance
            
            if i != self.getNumberOfPayments() - 1.0:
                principal = self.payment - monthlyInterest
                
            else:
                principal = self.loanBalance
                self.payment = self.loanBalance + monthlyInterest
            
            self.loanBalance -= principal
            print(self.payment)

            file.write("Month %d: Principal = %s,  Interest = %f,  Loan Balance: %f\n" % (i+1, str(round(principal,2)), monthlyInterest.__round__(2), self.loanBalance.__round__(2)))
        


if __name__ == '__main__':
    print('Mod2 UnitTest!')