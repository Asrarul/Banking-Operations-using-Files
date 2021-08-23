def Withdraw(User):
    i,file='',''
    with open("Registration.txt",'r+') as f:
        Usr=f.readlines()
        for i in Usr:
            if User==i: 
                while(True):
                    try: 
                        w_amt=float(input(' Enter the amount to Withdraw  :  ')) 
                        break
                    except:
                        print(" ***Invalid Amount***\n")
                Usr1=i.split('-')
                if float(Usr1[3])<(w_amt+500.0):
                    print('\n ****Your Balance is Low****')
                    return User
                else:    
                    w_amt1=float(Usr1[3])-w_amt
                    i=i.replace(Usr1[3],str(w_amt1))
                    break
    with open("Registration.txt",'r+') as f:
        file=f.read()
        file=file.replace(User,i)
    with open("Registration.txt",'w') as f:
        f.write(file)
    return i