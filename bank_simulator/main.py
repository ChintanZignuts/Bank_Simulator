from models import BankAccount

def main():
    bank = BankAccount()

    while True:
        print("\n==== Bank Account Simulator ====")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Delete Account")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter account holder's name: ")
            deposit = float(input("Enter initial deposit: "))
            pin = input("Set a 4-digit PIN: ")
            bank.create_account(name, deposit,pin)

        elif choice == "2":
            acc_num = int(input("Enter account number: "))
            amount = float(input("Enter deposit amount: "))
            bank.deposit(acc_num, amount)

        elif choice == "3":
            acc_num = int(input("Enter account number: "))
            amount = float(input("Enter withdrawal amount: "))
            pin = input("Enter your 4-digit PIN for authentication: ")
            bank.withdraw(acc_num, amount, pin)

        elif choice == "4":
            acc_num = int(input("Enter account number: "))
            bank.check_balance(acc_num)

        elif choice == "5":
            acc_num = int(input("Enter account number: "))
            pin = input("Enter your 4-digit PIN for authentication: ")
            bank.delete_account(acc_num, pin)

        elif choice == "6":
            print("Exiting program. Thank you!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()