def login():
    User=''
    with open("Registration.txt",'r+') as f:
        usr_name=f.readlines()
        flag=True
        #print(usr_name)
        while flag:
            user_name = input('Username : ')
            pass_word = input('Password : ')
            j=-1
            for i in usr_name:
                j=j+1
                i=i.split('-')
                if(i[1]==user_name):
                    User=usr_name[j]
                    if(i[2]==pass_word):
                        print('\n++++++Welcome '+i[0]+'++++++')
                        flag=False
                        break
                    else:
                        print('\n*****Invalid Password*****\n')
                        flag=True
                        break
            else:
                print('\n*****Username not Found*****\n')
                flag=True
    return User