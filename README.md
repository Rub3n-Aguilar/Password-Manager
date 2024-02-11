# Password-Manager
Simple Password Manager using bcrypt

This Python script implements a basic command-line password manager using the bcrypt library for secure password hashing and the getpass module for masked password input.

Features:
Account Creation: Users can create a new account by entering a username and password. The password is securely hashed using bcrypt before being stored.
User Login: Registered users can log in by entering their username and password. Password input is masked to protect user privacy.
Password Hashing: Passwords are securely hashed using the bcrypt algorithm, ensuring that sensitive information is protected even if the database is compromised.
User-Friendly Interface: The command-line interface guides users through account creation and login processes with clear prompts and messages.

Requirements:
Python 3
bcrypt library (install using pip install bcrypt)
