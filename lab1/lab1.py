#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Oskar Åkergren
Mac OS X 10.9.5
Python 3.4.1
"""

def main():
    while True:
        user_choice = input("Hej, ska det vara hel- eller flyttalsdivision? (h/f):"
                            ).lower()

        if user_choice != "h" and user_choice != "f":
            print("Tyvärr, dina möjliga val är h/H eller f/F")

        elif user_choice == "h":
            intnum()
            break

        else:
            floatnum()
            break


def intnum():
    try:
        dividend = int(input("Skriv in din dividend:  "))
        divisor = int(input("Skriv in din divisor:  "))
        prettyprint(dividend, divisor)
    except:
        print("Ange ett heltal")
        intnum()


def floatnum():
    try:
        dividend = float(input("Skriv in din dividend:  "))
        divisor = float(input("Skriv in din divisor:  "))
        prettyprint(dividend, divisor)
    except:
        print("Ange ett flyttal")
        floatnum()


def prettyprint(dividend, divisor):
    print(
        "\tResultatet av %g / %g = %g" %
        (dividend, divisor, (dividend / divisor))
    )

main()
