# ATM System (Python)

This project is a simulation of an Automated Teller Machine (ATM) system built using Python. It allows users to create accounts, log in securely, perform financial transactions, and store data persistently. The system is designed to resemble basic ATM functionality seen in real banking systems. The bank used as the project reference is **Fidelity Bank**.

## Features

- User Sign-Up and Login with PIN Authentication  
- Account Lockout After 3 Failed PIN Attempts  
- Check Account Balance  
- Deposit Money  
- Withdraw Money with Insufficient Balance Handling  
- Change PIN  
- View Transaction History with Timestamps  
- Export Transaction History to a Text File  
- Data Stored Permanently Using JSON

## File Structure

ATM_PROJECT/
│
├── atm.py # Main application file
├── data.json # User data storage file
├── history_<username>.txt (generated upon export)
└── README.md # Project documentation


## Requirements

- Python 3.x
- No external libraries required (uses only built-in modules)

## How to Run the Program

1. Open the project folder in a terminal or VS Code.
2. Run the program using:


3. Follow the on-screen instructions:
   - If you are a new user, sign up with your name and 4-digit PIN.
   - If you already have an account, log in and access the ATM menu.

## Data Storage

All user account data, balances, PINs, and transaction logs are saved in `data.json`.  
This allows the program to retain account information even after closing the application.

## Example ATM Menu

========== ATM MENU ==========

1.Check Balance

2.Deposit Money

3.Withdraw Money

4.Change PIN

5.Exit

6.View Transaction History

7.Export Transaction History


## Project Purpose

This project demonstrates:
- Python data structures (dictionaries, lists)
- Control flow (if/else, loops)
- File handling (read/write JSON and text files)
- Basic authentication logic
- Simple financial computation and validation

It is suitable for:
- Python beginners building their first real-world project
- Students preparing portfolio projects
- Demonstrating understanding of core programming concepts


## Author
Developed by **Abdulsamad**  
Fidelity Bank ATM Simulation Project

## GitHub
**GitHub Profile:** https://github.com/Ramee4sure
