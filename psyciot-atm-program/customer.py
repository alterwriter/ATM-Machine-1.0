#program for Customer (Nasabah) -- directed by Clone Writer / Ananda Fikri Ijlal Akbar

from atm_card import ATMcard

class Customer:
    def __init__(self, id, custPin = 1234, custBalance = 100000):
        self.id = id
        self.custPin = custPin
        self.custBalance = custBalance
    
    def checkId(self):
        return self.id
    
    def checkPIN(self):
        return self.custPin
    
    def checkBalance(self):
        return self.custBalance
    
    def tarikTunai(self, nominal):
        self.custBalance -= nominal
    
    def tabungTunai(self, nominal):
        self.custBalance += nominal
