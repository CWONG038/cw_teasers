# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 12:22:25 2021

@author: chris
"""


def format_amount(amount):
    raw_result = None
    while True:
        try:
            raw_result = float(input(amount))
        except ValueError:
            print("Please enter a valid number again.")
        else:
            if isinstance(raw_result, float):
                return "${:.2f}".format(raw_result)


def main():
    amount_spent = format_amount("Enter spending amount: ")
    print(amount_spent)


if __name__ == "__main__":
    main()
