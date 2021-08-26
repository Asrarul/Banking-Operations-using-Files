from Account_number import *


def new_user():
    flag = True
    with open("Database.txt", 'r+') as f:
        usr_name = (f.readlines())
        name = input("Name        : ")

        while flag:
            user_name = input('Username    : ')
            for i in usr_name:
                i = i.split('-')
                # print(i[1])
                if i[1] == user_name:
                    flag = True
                    print('\n*******Username already exists*******')
                    print('**************Try again***************\n')
                    break
            else:
                flag = False

        flag = True
        while flag:
            print('''\nYour password should atleast have 8 characters long,
              should atleast contain one Uppercase letter,
              should atleast contain one Special character
              ( !, @, #, $, %, *),
              should atleast contain one Number\n''')
            pass_word = input('Create new password : ')
            if len(pass_word) < 8:
                print("\n***Your Password should atleast contain 8 characters***")
            else:
                i, j, k = 0, 0, 0
                for x in pass_word:
                    if x >= '0' and x <= '9':
                        i += 1
                    elif x >= 'A' and x <= 'Z':
                        j += 1
                    elif x in ['!', '@', '#', '$', '%', '*']:
                        k += 1
                if i < 1 or j < 1 or k < 1:
                    print("\n*********Weak Password**********")
                    print("*************Try again************")
                    flag = True
                else:
                    flag = False

        flag = True
        while flag:
            pass_word2 = input("Re-Enter Password   : ")
            if pass_word == pass_word2:
                flag = False
            else:
                print('\n****Passwords mismatch****')
                print('*********Try again***********\n')
                flag = True

        flag = True
        while flag:
            try:
                print("\n****Deposit amount should be atleast ₹500.00****\n")
                Deposit = float(input('Deposit amount : '))
                if Deposit >= 500:
                    flag = False
                else:
                    flag = True

            except:
                print('\n***Invalid Amount***')
                flag = True

        flag = True
        while flag:
            try:
                Ph_no = int(input('\nPhone Number   : '))
                flag = False
            except:
                print('\n***Invalid Number***')
                flag = True

        flag = True
        while flag:
            location = input("\nLocation       : ")
            if location == None:
                print(type(location))
                print('\n***Invalid Location***')
                flag = True
            else:
                flag = False

        flag = True
        while flag:
            try:
                Pincode = int(input('\nPincode        : '))
                flag = False
            except:
                print('\n***Invalid Pincode***')
                flag = True

        Acc_no = Accno()
        f.write('-'.join([name, user_name, pass_word, str(Deposit),
                str(Ph_no), location, str(Pincode), str(Acc_no)]))
        f.write('-\n')
