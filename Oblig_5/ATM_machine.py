from Account_class import Account as Ac

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
def something():
    pass

def main():
    
    
    pass

if __name__ == "__main__":
    main()