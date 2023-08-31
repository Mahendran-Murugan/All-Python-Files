import random


class Bank:
    def __init__(self):
        self.bal = int(input('Enter the balance in your account:'))
        self.usr_name = input('Enter your Username:')
        self.usr_password = input('Enter your Password:')
        self.r = random.randint(100000, 999999)

    def check(self):
        print('\nEnter your Login details\n')
        chk_usr_name = input('Enter your Username:')
        chk_usr_password = input('Enter your Password:')
        if self.usr_name == chk_usr_name and self.usr_password == chk_usr_password:
            print('The one time password(OTP) is:', self.r)
            chk_r = int(input('Enter the OTP:'))
            if self.r == chk_r:
                print('\nLogin Successful\n')
                return True
            else:
                print('The OTP is Invalid')
        else:
            print('Invalid Username or Password')

    def bal_enquiry(self):
        chk = self.check()
        if chk:
            print('The balance in your account is:', self.bal)
        else:
            print('Operation Failed')

    def deposit(self):
        chk = self.check()
        if chk:
            dep_amount = int(input('Enter the amount to be deposited:'))
            self.bal += dep_amount
            print('The balance in your account is:', self.bal)
        else:
            print('Operation Failed')

    def withdraw(self):
        chk = self.check()
        if chk:
            with_amount = int(input('Enter the amount to be withdraw:'))
            self.bal -= with_amount
            print('The balance in your account is:', self.bal)
        else:
            print('Operation Failed')


obj = Bank()
while True:
    print("""The options are
                        1.Deposit
                        2.Withdraw
                        3.Balance Enquiry""")
    ch = int(input('Enter your choice:'))
    if ch == 1:
        obj.deposit()
    elif ch == 2:
        obj.withdraw()
    elif ch == 3:
        obj.bal_enquiry()
    else:
        print('Enter a valid input')
