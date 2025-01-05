
from accounts import load_account_file,create_account,login
from transactions import deposit,withdraw


def main():
    accounts=load_account_file()
    while True:
        print("Welcome to the Banking System!")
        print("1.Create Account")
        print("2.Login")
        print("3.Exit")
        choices=input("Enter your choice:")
        if choices=="1":
            create_account(accounts)
        elif choices=="2":
            acc_num=login(accounts)
            if acc_num:
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Logout")
                    sub_choice=input("Enter your choice:")
                    if sub_choice=="1":
                        deposit(accounts,acc_num)
                    elif sub_choice=="2":
                        withdraw(accounts,acc_num)
                    elif sub_choice=="3":
                        print("Logged out successfully.")
                        break
                    else:
                        print("Invalid choice. Try again")
        elif choices=="3":
            print("Exit")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__=="__main__":
    main()

