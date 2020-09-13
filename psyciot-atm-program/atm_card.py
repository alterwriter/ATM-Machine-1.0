#program for ATM Card -- directed by Clone Writer / Ananda Fikri Ijlal Akbar

class ATMcard:
    
    def __init__(self, defaultPin, defaultBalance):
        self.defaultPin = defaultPin
        self.defaultBalance = defaultBalance
    
    def firstPIN(self):
        return self.defaultPin
    
    def firstBalance(self):
        return self.defaultBalance
