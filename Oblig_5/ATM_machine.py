from Account_class import Account

def main_menu():
    while True:
        print("\nMain menu")
        print("1: Check balance")
        print("2: Withdraw")
        print("3: Deposit")
        print("4: Exit")

        choice = int(input("Enter a choice: "))
        if choice < 1 or choice > 4:
            print("Wrong choice, try again:", end = '')
        else:
            break

    return choice

def choice_handler(accounts, choice, id):
    if choice == 1:
        print(f"The balance is {accounts[id].balance}")

    if choice == 2:
        amount_to_withdraw = int(input("Enter an amount to withdraw: "))
        accounts[id].withdraw(amount_to_withdraw)

    if choice == 3:
        amount_to_deposit = int(input("Enter an amount to deposit: "))
        accounts[id].deposit(amount_to_deposit)


def main_system(accounts):   
    while True:
        user_id = int(input("Enter an id please: "))
        
        if user_id < 0 or user_id > 9:
            print("Innvalid id, please try again.")
        else:
            break

    while True:
        choice = main_menu()
        if choice == 4:
            break
        choice_handler(accounts, choice, user_id)


def main():
    accounts = []
    for x in range(10):
        accounts.append(Account(x, 100, 0))
    
    while True:
        main_system(accounts)
    

if __name__ == "__main__":
    main()
