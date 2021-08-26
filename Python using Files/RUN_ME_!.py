from Registration import *
from login import *
from Check_details import *
from Deposit import *
from Withdraw import *
from View_balance import *


print('\n    ++++++Banking++++++   ')

flag=True
while(flag):
    opt=int(input('''\n( 1 ) New user\n( 2 ) Login\n( 3 ) Exit\n  '''))
    if opt==1:
        new_user()
        flag=True
    elif opt==2:
        User=login()
        flag=False
    elif opt==3:
        break
    else:
        print('\n****Invalid Request****')
        print('\n******Try Again!*******')

flag=True
while flag:
    opr=int(input('''\n ( 1 ) View Account Details\n ( 2 ) Deposit\n ( 3 ) Withdraw\n ( 4 ) View Balance\n ( 5 ) Exit\n   '''))

    if opr==1:
        view_details(User)
        flag=True
    elif opr==2:
        User=Deposit(User)
        flag=True
    elif opr==3:
        User=Withdraw(User)
        flag=True
    elif opr==4:
        View_balance(User)
        flag=True
    elif opr==5:
        break
    else:
        print("\n*****Invalid Request*****\n")
        flag=True
