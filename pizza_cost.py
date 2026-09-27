#!/usr/bin/env python3
# Created By: Victor V-C
# Date: 09 25, 2026
# This code will calculate the total price of pizza based on the given diameter from the user

import constants


def main():
    # Get the diameter of pizza from the user
    diameter = int(input("Enter diameter of pizza (incs): "))

    # Calculate the Subtotal, tax and total
    subTotal = (
        constants.MATERIALS * diameter
        + constants.LABOUR
        + constants.RENT
        + (constants.PIZZA_COST * diameter)
    )
    tax = subTotal * constants.HST
    total = subTotal + tax

    # Display the total
    print("Price of pizza: ${:.2f}".format(total))


if __name__ == "__main__":
    main()
