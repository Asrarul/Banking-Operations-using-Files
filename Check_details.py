def view_details (User):
    User=User.split('-')
    print('\n Name             :  '+User[0])
    print(' Account Number   :  '+User[-2])
    print(' Phone Number     :  '+User[4])
    print(' Location         :  '+User[5])
    print(' Pincode          :  '+User[6])