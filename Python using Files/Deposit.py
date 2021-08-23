def Deposit(User):
    i, file = '', ''
    with open("Registration.txt", 'r+') as f:
        Usr = f.readlines()
        for i in Usr:
            if User == i:
                while(True):
                    try:
                        d_amt = float(
                            input(' Enter the amount to Deposit  :  '))
                        break
                    except:
                        print(" ***Invalid Amount***\n")
                Usr1 = i.split('-')
                d_amt1 = float(Usr1[3])+d_amt
                i = i.replace(Usr1[3], str(d_amt1))
                break
    with open("Registration.txt", 'r+') as f:
        file = f.read()
        file = file.replace(User, i)
    with open("Registration.txt", 'w') as f:
        f.write(file)
    return i
