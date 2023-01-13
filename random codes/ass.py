
import random
# from string import digits
# import string
import time

def otp_gen(n):
    otp = ""
    
    for i in range(n):
     otp += str(random.choice(range(10)))
    #  random.seed(0)
    return  otp


data = {}
balance = 0
print("*"*27)
print("Welcome to GiveawayHub! \nYour Best choice in Finance")
print("*"*27)

while True:
    print("Welcome!!! What would you like to do?")
    print("1. Login \n2. SignUp \n3. Quit")
    user_input = input("Pick 1 for Login or 2 for SignUp \n :>>")
    # print(user_input)

    if user_input == "1":
            print("\nPlease enter your account id.")
            acc_id = input("::>")
            acc_data = data.get(acc_id, False) 
            if acc_data:
             print("Enter Login Pin")
            login = input("::>")
            login_data = data[acc_id].get("login", False)
            if login_data == login:
               while True: 
                print(f"Welcome to GiveawayHub! {first_name}, What will you like to do?")
                print("1. Deposit Money \n2. Withdraw Money \n3. Transfer Money \n4. Check Account Balance \n5. Quit")
                user_option = input("::>")
                if user_option == "1":
                    print("You've selected the deposit option")
                    print("How much will you like to deposit")
                    deposit_amt = int(input("::>"))
                    print("Verifying...")
                    print("Put pin info here")
                    trans_pin = input("::>")
                    trans_data = data[acc_id].get("transaction_pin", False)
                    if trans_data == trans_pin:
                     data[acc_id]["balance"] += deposit_amt
                     print("Deposit Successful!")
                     time.sleep(2)
                     print(f"You've deposited ${deposit_amt} successfully!")
                    #  print(data)
                    else:
                     print("Invalid Pin") 
                elif user_option =="2":
                        print("You've selected the withdraw option")
                        print("How much will you like to withdraw")
                        withdraw_amt = int(input("::>"))
                        print("Verifying...")
                        print("Put pin info here")
                        trans_pin = input("::>")
                        trans_data = data[acc_id].get("transaction_pin", False)
                        if trans_data == trans_pin:
                           if data[acc_id]["balance"] >= withdraw_amt:
                            data[acc_id]["balance"] -= withdraw_amt
                            print("Transaction Successful...")
                            time.sleep(2)
                            print(f"You've withdrawn ${withdraw_amt} successfully")
                            # print(data)
                           else:
                            print("Not enough balance!")  
                        else: 
                             print("Invalid Pin")       
                elif user_option == "3":
                    print("You've selected the transfer option") 
                    print("How much will you like to transfer")
                    transfer_amt = int(input("::>"))
                    print("Enter recipient id")
                    res_id = input("::>")
                    res_data = data.get(res_id)
                    if res_data:
                        print("Verifying Recipent...")
                        time.sleep(2)
                        print("Recipent has been confirmed!")  
                        time.sleep(2) 
                        print("Transaction in progress...") 
                        time.sleep(2)
                        balance = data[res_id]["balance"]
                        if data[acc_id]["balance"] >= transfer_amt:
                           data[acc_id]["balance"] -= transfer_amt 
                           data[res_id]["balance"] += transfer_amt
                           print("Transaction Successful!") 
                           print(f"You've transfered ${transfer_amt} successfully")
                           print(data)
                        else:
                            print("Not enough money")
                    else: 
                        print("User not found")
                    
                    
                    
                  
            
                elif user_option == "4":
                    print("You've selected the balance option")
                    print("Would you like to proceed (Y/N)")
                    balance_opt = input("::>").lower() 
                    if balance_opt == "y":
                       print("loading...")
                       time.sleep(2)
                       acc_balance = data[acc_id].get("balance")
                       time.sleep(2)
                       print(f"Your account balance is ${acc_balance}")
                    #    print(data)
                    elif balance_opt == "n":
                        print("loading...")
                        pass
                    else:
                        print("Not an option") 
                elif user_option == "5":
                    break      
            else:
                 print("Invalid login information")

        

    elif user_input == "2":
        print("Pls enter your first name")
        first_name = input("::>").title()
        print("Pls enter your last name")
        last_name = input("::>").title()
        print("Input login pin")
        login_pin = input("::>")
        print("Input transaction pin")
        trans_pin = input("::>")
        acc_id ='0' + str(otp_gen(9))
        data[acc_id] = {"first_name": first_name,
                         "last_name": last_name,
                         "login": login_pin,
                         "transaction_pin": trans_pin,
                         "balance" : 0
                         }
        print("Creating account...")
        time.sleep(3)
        print("Completing setup...")
        time.sleep(2)
        print(f"\nWelcome {first_name}!\nYou account has been created and activated. You account id is {acc_id}\nDo giveaway!\nRPS Support.\n")
    if user_input == 3:
        break

    # data= {acc_id: {"first_name": first_name, "last_name": last_name, "login": login_pin, "transaction_pin": trans_pin, "balance" : 0 }}
    