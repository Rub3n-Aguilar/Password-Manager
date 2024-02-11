import bcrypt
import getpass

password_manager = {}

def create_account():
    print("\nCreate Account")
    username = input("Please enter a username: ")
    password = getpass.getpass("Please enter a password: ")
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    password_manager[username] = hashed_password
    print("Account created successfully!")

def login():
    print("\nUser Login")
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = password_manager.get(username)
    if hashed_password and bcrypt.checkpw(password.encode(), hashed_password):
        print("Login successful!")
    else:
        print("Invalid username or password.")

def main():
    while True:
        choice = input("Enter 1 to create an account, 2 to login, or 0 to exit: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()