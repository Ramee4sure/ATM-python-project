import json
import os
from datetime import datetime

data_file = "data.json"

# Load data from file or create new data structure
if os.path.exists(data_file):
    with open(data_file, "r") as file:
        users = json.load(file)
else:
    users = {}
    with open(data_file, "w") as file:
        json.dump(users, file, indent=4)

# Backfill: ensure every user record has a transactions list (prevents KeyError on older data)
for u in users.values():
    if "transactions" not in u:
        u["transactions"] = []
# persist any backfilled changes
with open(data_file, "w") as file:
    json.dump(users, file, indent=4)

# Welcome message
print("\n==============================")
print("      TRUST BANK ATM")
print("==============================")


have_account = input("Do you have an account? (yes/no): ").strip().lower()

if have_account == "no":
    name = input("Enter your name to sign up: ").strip()
    if name in users:
        print("Account already exists. Please log in.")
        # fall through to login prompt below
    else:
        try:
            pin = int(input("Set a 4-digit PIN: "))
        except ValueError:
            print("Invalid PIN. PIN must be numbers only.")
            exit()
        users[name] = {"pin": pin, "balance": 0, "transactions": []}
        with open(data_file, "w") as file:
            json.dump(users, file, indent=4)
        print("Account created successfully! Please log in.")
        # continue to login prompt so user can log in immediately

elif have_account == "yes":
    # proceed to login
    pass

else:
    print("Invalid response! Please enter yes or no.")
    exit()

# login system
name = input("Please enter your name to log in: ").strip()
if name in users:
   attempts = 0      
   while attempts < 3:
        entered_pin = int(input("Enter your PIN: "))
        if entered_pin == users[name]["pin"]:
            print(f"Welcome, {name}!")

            while True:
                print("\n========== ATM MENU ==========")
                print("1. Check Balance")
                print("2. Deposit Money")
                print("3. Withdraw Money")
                print("4. Change PIN")
                print("5. Exit")
                print("6. View Transaction History")
                print("7. Export Transactions History")
                print("==============================")


                choice = input("Enter your choice (1–5): ")

                if choice == "1":
                    print(f"\nAVAILABLE BALANCE: ₦{users[name]['balance']}\n")


                elif choice == "2":
                    deposit = int(input("Enter deposit amount: "))
                    users[name]["balance"] += deposit
                    users[name]["transactions"].append(f"Deposited ₦{deposit} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                    print(f"₦{deposit} deposited successfully! New balance: ₦{users[name]['balance']}")
                    print(f"RECEIPT: Deposited ₦{deposit} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

                elif choice == "3":
                    withdrawal = int(input("Enter withdrawal amount: "))
                    if withdrawal > users[name]["balance"]:
                        print("Insufficient balance!")
                    else:
                        users[name]["balance"] -= withdrawal
                        users[name]["transactions"].append(f"Withdrew ₦{withdrawal} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                        print(f"₦{withdrawal} withdrawn successfully! New balance: ₦{users[name]['balance']}")
                        print(f"RECEIPT: Withdrew ₦{withdrawal} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                elif choice == "4":
                    new_pin = int(input("Enter your new PIN: "))
                    users[name]["pin"] = new_pin
                    print("PIN changed successfully!")

                elif choice == "5":
                    with open(data_file, "w") as file:
                        json.dump(users, file, indent=4)
                    print("Your data has been saved. Goodbye!")
                    

                elif choice == "6":
                    print("\n--- Transaction History ---")
                    if users[name]["transactions"]:
                        for t in users[name]["transactions"]:
                            print("-", t)
                    else:
                        print("No transactions yet.")

                elif choice == "7":
                    filename = f"history_{name}.txt"
                    with open(filename, "w") as f:
                        if users[name]["transactions"]:
                            for t in users[name]["transactions"]:
                                f.write(t + "\n")
                        else:
                            f.write("No transactions recorded yet.\n")
                    print(f"Transaction history exported successfully as '{filename}'.")

                else:
                    print("Invalid choice! Please enter 1–7.")


        else:
            attempts += 1
            print("Incorrect PIN!")
            if attempts == 3:
                print("Too many incorrect attempts! Account locked.")
                break
else:
    print("Account not found. Please sign up first.")


        
                                                                                    
