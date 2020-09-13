#program for ATM Machine -- directed by Clone Writer / Ananda Fikri Ijlal Akbar

import random
import datetime
from customer import Customer

atm = Customer(id)

while True:
    id = int(input('Masukkan PIN Anda: '))
    trial = 0

    while (id != int(atm.checkPIN()) and trial < 3 ):
        id = int(input("PIN anda salah, silahkan masukkan lagi: "))
        trial += 1

        if trial == 3:
            print("error, silahkan ambil kartu dan coba lagi.")
            exit()

    while True:
        print("Welcome to PSYCIOT BANK...")
        print("please choose: \n1 - Balance Checking\n2 - Withdraw\n3 - Save Balance\n4 - change PIN\n5 - exit")
        inputMenu = int(input("\nSelect Menu: "))

        if inputMenu == 1:
            print('Your Balance is: ' + str(atm.checkBalance()) + "\n")
        elif inputMenu == 2:
            nominal = float(input("please enter your balance: "))
            balanceVerify = input("are you sure want to withdraw " + str(nominal) + " ? y/n ")

            if balanceVerify == "y":
                print("Saldo anda adalah: " + str(atm.checkBalance()) + '\n')
            else:
                break

            if nominal < atm.checkBalance():
                atm.tarikTunai(nominal)
                print('Transaksi anda telah berhasil.')
                print('saldo yang tersisa adalah ' + str(atm.checkBalance()) + "\n")
            else:
                print("Transaction is incomplete")
                print("=========================")
                print("Please add your balance\n")
        elif inputMenu == 3:
            nominal = float(input("please enter your balance: "))
            balanceUpdate = input("are you sure want to save " + str(nominal) + " ? y/n ")

            if balanceUpdate == 'y':
                atm.tabungTunai(nominal)
                print("Your balance is: " + str(atm.checkBalance())+ '\n')

        elif inputMenu == 4:
            verifyPIN = int(input("Verify your PIN: "))
            
            while verifyPIN != atm.checkPIN():
                print('incorrect PIN, please re-enter: ')
            
            updatePIN = int(input("enter the new PIN: "))
            print("your pin has been changed.")

            verifyNewPIN = int(input("re-enter your new PIN: "))
            if verifyNewPIN == updatePIN:
                print("new PIN has been successful\n")
            else:
                print("incorrect PIN\n")

        elif inputMenu == 5:
            print("balance inquiry will be printed out \nPlease save this approval\nAs your transaction history")
            print("Record Number\t: ", random.randint(10000,1000000))
            print("date\t\t: ", datetime.datetime.now())
            print("Balance\t\t: ", int(atm.checkBalance()))
            print("====================================")
            print("thank you for accessing PSYCIOT BANK")
            exit()

        else:
            print("Error detected!!!")

