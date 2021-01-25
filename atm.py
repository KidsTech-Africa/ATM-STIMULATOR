import random
print ("WELCOME TO GTBANK ATM")
accountnumber = [1007865126,2084542995,1195342344]
accountname = ["Olaoluwa Tomiwa Adewuyi","Oyewale Abdulganiyu Olawale","Ishola Emmanuel"]
pin = [1234,2102,4522]
balance =[20000,40000,50000]
print("Insert Your Card: Press 1 to Insert Your Card")
insertcard = int(input())
if insertcard == 1:
    print("Enter Your Pin")
    userpin = int(input())
    counter = 0
    invalidpin = 0
    for x in pin:
        if(userpin == x):
            print("Card Pin is Correct")
            print("Welcome",accountname[counter])
            print("Enter 1 For Withdraw")
            print("Enter 2 For Deposit")
            print("Enter 3 For Balance")
            useraction = int(input())
            if useraction == 1:
                print("Enter Amount to Withdraw")
                
                amount = int(input())
                if amount > balance[counter]:
                    print("Insufficient Fund")
                elif amount <= balance[counter]:
                    withdrawamount = balance[counter] - amount
                    print("Transaction Successful")
                    print("Your total remaining Balance is",withdrawamount)
                    
                    
            elif useraction == 2:
                print("Enter Amount to Depsoit")

                amount = int(input())
                balance[counter] = balance[counter] + amount
                print("Deposit Succesful, Your Balance is",balance[counter])


            elif useraction == 3:
                print("Enter  your 4 digit pin to continue:")
                balpin = int(input())
                if(userpin == x):
                    withdrawalamount = balance[counter]
                    print("your total remaining balance=",withdrawalamount)
                    
                
            
            break
        elif(userpin != x):
            invalidpin = invalidpin + 1
        counter= counter + 1
    if invalidpin == 3:
        print("Wrong Pin")
        print("Enter Your Pin Again")
        userpin = int(input())
        counter = 0
        invalidpin = 0
        for x in pin:
            if(userpin == x):
                print("Card Pin is Correct")
                print("Welcome",accountname[counter])
                print("Enter 1 For Withdraw")
                print("Enter 2 For Deposit")
                useraction = int(input())
                if useraction == 1:
                    print("Enter Amount to Withdraw")
                    amount = int(input())
                    if amount > balance[counter]:
                        print("Insufficient Fund")
                    elif amount <= balance[counter]:
                        withdrawamount = balance[counter] - amount
                        print("Transaction Successful")
                        print("Your Balance is",withdrawamount)
                        
                elif useraction == 2:
                    print("Enter Amount to Depsoit")

                    amount = int(input())
                    balance[counter] = balance[counter] + amount
                    print("Deposit Succesful, Your Balance is",balance[counter])
                    
                break
            elif(userpin != x):
                invalidpin = invalidpin + 1
            counter= counter + 1
        
            
    
    
elif insertcard != 1:
    print("Invalid Input")

 
