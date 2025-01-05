from accounts import ACCOUNTS_FILE
from datetime import date

TRANSACTIONS_FILE="transactions.txt"

def log_transaction(acc_num,transaction_type, amount):
    #print("log-transaction")
    with open(TRANSACTIONS_FILE,"a") as f:
        dates = date.today()
        # print(dates)
        f.write(f"{acc_num},{transaction_type},{amount},{dates}\n")

def deposit(accounts,acc_num):
    #print("Deposit")
    amount=float(input("Enter amount to deposit:"))
    av_bal=float(accounts[acc_num]["balance"]) + amount
    accounts[acc_num]["balance"] = str(av_bal)
    print(f"Deposit successful! Current balance: {accounts[acc_num]['balance']}")
    log_transaction(acc_num,"Deposit",str(amount))
    update_account_file(accounts)

def withdraw(accounts,acc_num):
    #print("Withdraw")
    amount = float(input("Enter amount to withdraw:"))
    if amount>float(accounts[acc_num]["balance"]):
        print("Insufficient balance!")
    else:
        #accounts[acc_num]["balance"] -= amount
        av_bal = float(accounts[acc_num]["balance"]) - amount
        accounts[acc_num]["balance"] = str(av_bal)
        print(f"Withdrawal successful! Current balance: {accounts[acc_num]['balance']}")
        log_transaction(acc_num, "Withdrawal", str(amount))
        update_account_file(accounts)

def update_account_file(accounts):
    #print("update-account-file")
    with open("accounts.txt", "w") as f:
        for acc_num, details in accounts.items():
            f.write(f"{acc_num},{details['name']},{details['password']},{details['balance']}\n")

