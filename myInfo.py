"""
Author: Jazz Courter
Date Written: 10/25/2024
Assignment: Module 01 Practice Exercise 1-1
This program is designed to ask for the input of
name, address, and phone number, and then print them.
"""

while True:
    # Input name, addres, and phone number
    strName = input("Enter your name: ")
    strAddress = input ("Enter your address: ")
    strPhone = input("Enter your phone number: ")

    # Print the input values
    print("Name: ", strName)
    print("Address: ", strAddress)
    print("Phone number: ", strPhone)

    #Ask user if they want to continue
    response = input("\nDo you want to add another contact? (yes/no): ")

    #Break loop if user chooses no
    if response.lower() != "yes":
        break
