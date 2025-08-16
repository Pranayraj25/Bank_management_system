import sqlite3

# ----------------------------
# Database setup
# ----------------------------
def create_table():
    conn = sqlite3.connect("bank.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            balance REAL DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()


# ----------------------------
# Core Banking Functions
# ----------------------------
def create_account():
    name = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Deposit Amount: "))

    conn = sqlite3.connect("bank.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", (name, balance))
    conn.commit()
    conn.close()
    print(f"✅ Account created for {name} with balance {balance}")


def view_accounts():
    conn = sqlite3.connect("bank.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM accounts")
    rows = cur.fetchall()
    conn.close()

    print("\n📋 Account List:")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Balance: {row[2]}")
    if not rows:
        print("⚠️ No accounts found.")


def deposit():
    aid = int(input("Enter Account ID: "))
    amt = float(input("Enter Deposit Amount: "))

    conn = sqlite3.connect("bank.db")
    cur = conn.cursor()
    cur.execute("UPDATE accounts SET balance = balance + ? WHERE id = ?", (amt, aid))
    conn.commit()
    conn.close()
    print(f"💰 Deposited {amt} into Account {aid}")


def withdraw():
    aid = int(input("Enter Account ID: "))
    amt = float(input("Enter Withdraw Amount: "))

    conn = sqlite3.connect("bank.db")
    cur = conn.cursor()
    cur.execute("SELECT balance FROM accounts WHERE id = ?", (aid,))
    row = cur.fetchone()

    if row and row[0] >= amt:
        cur.execute("UPDATE accounts SET balance = balance - ? WHERE id = ?", (amt, aid))
        conn.commit()
        print(f"💸 Withdrawn {amt} from Account {aid}")
    else:
        print("❌ Insufficient Balance or Invalid Account ID")

    conn.close()


def delete_account():
    aid = int(input("Enter Account ID to Delete: "))

    conn = sqlite3.connect("bank.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM accounts WHERE id = ?", (aid,))
    conn.commit()
    conn.close()
    print(f"🗑️ Account {aid} deleted (if it existed)")


# ----------------------------
# Menu Loop
# ----------------------------
def menu():
    create_table()  # Ensure DB exists

    while True:
        print("\n=== 🏦 Bank Management System ===")
        print("1. Create Account")
        print("2. View Accounts")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Delete Account")
        print("6. Exit")

        choice = input("Enter Choice (1-6): ")

        if choice == "1":
            create_account()
        elif choice == "2":
            view_accounts()
        elif choice == "3":
            deposit()
        elif choice == "4":
            withdraw()
        elif choice == "5":
            delete_account()
        elif choice == "6":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid Choice. Try again.")


if __name__ == "__main__":
    menu()
