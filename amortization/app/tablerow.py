class TableRow():
    month       = 0.0
    interest    = 0.0
    principal   = 0.0
    balance     = 0.0


    def __init__(self, month, interest, principal, balance):
        self.month      = month
        self.interest   = interest
        self.principal  = principal
        self.balance    = balance