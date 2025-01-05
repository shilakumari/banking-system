import os
import random

ACCOUNTS_FILE="accounts.txt"
def load_account_file():
    #print("loading account file.")
    accounts={}
    if os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE,"r") as f:
            for line in f:
                acc_num,name,password,balance=line.strip().split(",")
                accounts[acc_num]={
                    "name":name,
                    "password":password,
                    "balance":balance,
                }
    return  accounts

def save_account(acc_num,account):
    with open(ACCOUNTS_FILE,"a") as f:
        f.write(f"{acc_num},{account['name']},{account['password']},{account['balance']}\n")

def create_account(accounts):
    #print("Creating account")
    name = input("Enter your name:")
    initial_deposit = float(input("Enter your initial deposit:"))
    acc_num = ""
    for i in range(6):
        acc_num += str(random.randint(0, 9))
    password = input("Enter a password:")

    accounts[acc_num]={
        "name": name,
        "password": password,
        "balance": initial_deposit,
    }
    save_account(acc_num,accounts[acc_num])
    print(f"Account created successfully! account number:{acc_num}")
    print("(Account details saved to accounts.txt)")

def login(accounts):
    #print("Login")
    acc_num=input("Enter your account number:")
    password=input("Enter your password:")
    if acc_num in accounts and accounts[acc_num]["password"]==password:
        print("Login successful!")
        return acc_num
    else:
        print("Invalid account number or password.")
        return None


