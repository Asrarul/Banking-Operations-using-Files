def Accno():
    with open("Database.txt",'r+') as f:
        Acc_no=(f.readlines())
        try:
           Acc_no=Acc_no[-1]
           Acc_no=Acc_no.split('-')
        except:
           return 1250000001
        try:
            return int(Acc_no[-2])+1
        except:
            return 1250000001
