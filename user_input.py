"""
    Objective: To learn how to take user input in Python

    Write a program that asks the user for their name, age, and location and then prints out a personalized message.

    Instructions:
    Create a new Python file and name it "user_input.py"
    Use the input() function to ask the user for their name and store it in a variable called "name".
    Use the input() function to ask the user for their age and store it in a variable called "age".
    Use the input() function to ask the user for their location and store it in a variable called "location".
    Print out a personalized message using the user's name, age, and location. For example: "Hello [name], you are [age] years old and live in [location]."
    Save and run the program to see the output.
"""

print("---" * 10 + "\n")
name = input("Enter Your Name: ")
age = input("Enter Your Age: ")
location = input("Enter Your Location: ")

message = f"\nHello {name}, your are {age} years old and live in {location}"
print(message)
