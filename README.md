# Banking System
    : Developed a console-based Banking System that allows users to create accounts, perform banking transactions, and manage their finances. The project should include secure login functionality, transaction logging, and persistent storage of user and transaction data using file handling.

  # Required text files
    1. Problem.txt
    2. accounts.txt
    3. transactions.txt
  
  # Required Python Files
    1. main.py
    2. accounts.py
    3. transactions.py
  
  # main.py
    : It is a main file that runs first of this banking system console-based application.
    # Inherited Files
      1. accounts.py
      2. transactions.py
      It calls:-
        load_account_file() from accounts.py:
          To load account's details.
        create_account(accounts) from accounts.py:
          To create account.
        login(accounts) from account.py:
          To login for account operations.
          If login successful then we can withdraw or deposit amounts.
            i. Withdraw
              withdraw(accounts,acc_num) method called from transactions.py:
                To withdrawal the amount.
            ii. Deposit
              deposit(accounts,acc_num) method called from transactions.py:
                To deposit the amount.
            iii. Logout:
              When don't want deposit or withdrawal then simply logout.
        When login is unsuccessful then try again or exit from the application.
        
        
        
  
