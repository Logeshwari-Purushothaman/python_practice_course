from BankAccount import *

Logeshwari = BankAccount(1000,"Logeshwari")
Suresh = BankAccount(2000,"Suresh")

Logeshwari.get_balance()
Suresh.get_balance()
Logeshwari.deposit(500)
Suresh.deposit(20)
#Logeshwari.withdraw(100000000000)
Logeshwari.withdraw(120)
Logeshwari.transfer(200,Suresh)

print("------------")
Mani = InterestRewardsAcc(100,"Mani")
Mani.get_balance()
Mani.deposit(100)

print("------------")
Kani = SavingsAcct(1000,"Kani")
Kani.get_balance()
Kani.withdraw(100)
Kani.transfer(5,Logeshwari)


