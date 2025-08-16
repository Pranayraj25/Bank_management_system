# Bank Management System (Python + MySQL)

A simple command-line Bank Management System using Python and MySQL.

## Features

- Customer creation
- Account creation (Savings/Current)
- Deposit & Withdraw
- Balance inquiry
- Transaction history

## Setup Instructions

1. **Install MySQL** and create the database/tables:

    ```bash
    mysql -u root -p < database.sql
    ```

2. **Install dependencies:**

    ```bash
    pip install mysql-connector-python python-dotenv
    ```

3. **Set up environment variables:**

    - Copy `.env.example` to `.env` and fill in your MySQL credentials.

4. **Run the application:**

    ```bash
    python bank_management.py
    ```

## Notes

- For demo/learning purposes. No authentication or advanced validation.