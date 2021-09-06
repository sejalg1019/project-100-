class Atm(object):
    def __init__(self, name, cardNumber, pin): 
        self.name = name
        self.cardNumber = cardNumber
        self.pin = pin

    def checkBalance(self):
        print("Your balance is $50,000")    

    def cashWithdrawal(self, amount):
        newAmount = 50000 - amount
        print("You have withdrawn " + str(amount) + ". Your remaining balance is now " str(newAmount))

    def accessCard(self):
        putCard = input("Input Card number: ")
        putPin = input("Input Pin to access card: ")

        if putPin == self.pin:
            print("Pin successfully inputted")

        if not putPin == self.pin:
            print("Incorrect Pin")

    def main():
        accessCard()
        print("Choose your activity ")
        print("1. Balance Inquiry  2. Withdrawal")
        activity = int(input("Enter Activity Number: "))

        if(activity == 1):
            checkBalance()
        elif(activity == 2):
            amount = int(input("Enter amount: "))
            cashWithdrawal(amount)
        else: 
            print("Enter a Valid Number")
    
Kai = Atm("Kai", "1234567890", "1234")
Kai.main()

