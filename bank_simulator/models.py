from db import get_db_connection
from mysql.connector import Error

class BankAccount:
    def __init__(self):
        self.connection = get_db_connection()

    def create_account(self, name, initial_deposit, pin):
        if initial_deposit < 0:
            print("Initial deposit cannot be negative!")
            return

        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO accounts (name, balance, pin) VALUES (%s, %s, %s)"
            cursor.execute(query, (name, initial_deposit, pin))
            self.connection.commit()
            account_number = cursor.lastrowid
            print("--------------------------------")   
            print(f"Account created successfully for {name}!")
            print(f"Your Account Number: {account_number}")
            print(f"Initial Balance: ${initial_deposit:.2f}")
            print("--------------------------------")   
        except Error as e:
            print("Error:", e)

    def deposit(self, account_number, amount):
        if amount <= 0:
            print("Deposit amount must be positive!")
            return

        try:
            cursor = self.connection.cursor()

            cursor.execute("SELECT balance FROM accounts WHERE account_number = %s", (account_number,))
            result = cursor.fetchone()

            if not result:
                print("Error: Account not found!")
                return

            query = "UPDATE accounts SET balance = balance + %s WHERE account_number = %s"
            cursor.execute(query, (amount, account_number))
            self.connection.commit()
            print(f"Deposited ${amount:.2f} successfully!")

        except Error as e:
            print("Database error:", e)

    def withdraw(self, account_number, amount, pin):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return

        try:
            cursor = self.connection.cursor()
            
            # Verify PIN
            cursor.execute("SELECT balance, pin FROM accounts WHERE account_number = %s", (account_number,))
            result = cursor.fetchone()

            if not result:
                print("Error: Account not found!")
                return

            balance, stored_pin = result

            if stored_pin != pin:
                print("Error: Incorrect PIN! Withdrawal denied.")
                return

            if balance >= amount:
                query = "UPDATE accounts SET balance = balance - %s WHERE account_number = %s"
                cursor.execute(query, (amount, account_number))
                self.connection.commit()
                print(f"Withdrew ${amount:.2f} successfully!")
            else:
                print("Error: Insufficient balance!")

        except Error as e:
            print("Database error:", e)

    def check_balance(self, account_number):
        try:
            cursor = self.connection.cursor()
            query = "SELECT name, balance FROM accounts WHERE account_number = %s"
            cursor.execute(query, (account_number,))
            result = cursor.fetchone()

            if result:
                print(f"Account Holder: {result[0]}, Balance: ${result[1]:.2f}")
            else:
                print("Error: Account not found!")
        except Error as e:
            print("Database error:", e)

    def delete_account(self, account_number, pin):
        try:
            cursor = self.connection.cursor()

            # Verify PIN
            cursor.execute("SELECT pin FROM accounts WHERE account_number = %s", (account_number,))
            result = cursor.fetchone()

            if not result:
                print("Error: Account not found!")
                return

            stored_pin = result[0]

            if stored_pin != pin:
                print("Error: Incorrect PIN! Account deletion denied.")
                return

            query = "DELETE FROM accounts WHERE account_number = %s"
            cursor.execute(query, (account_number,))
            self.connection.commit()
            print("Account deleted successfully!")

        except Error as e:
            print("Database error:", e)