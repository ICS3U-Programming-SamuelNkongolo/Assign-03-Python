#!/usr/bin/env python3
# Created By: Samuel Nkongolo
# Date: Oct. 19, 2022
# This program asks the user to enter 3 numbers and tells them the smallest one


def main():

    # ask the user for 3 random users
    first = input("Enter your first number:")
    second = input("Enter your second number:")
    third = input("Enter your third number:")

# Calculate smallest number and display it
    if first < second:
        if first < third:
            print("The smallest number is", first)
        else:
            print("Smallest number is", third)
    else:
        if second < third:
            print("Smallest number is", second)
        else:
            print("Smallest number is", third)


if __name__ == "__main__":
    main()
