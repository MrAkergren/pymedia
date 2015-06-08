#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys

while True:
    user_choice = input("Vad vill du dela? heltal eller flyttal? (h/f)  ")\
                    .lower()
    
    if user_choice == "quit":
        sys.exit(1)

    elif user_choice != "h" and user_choice != "f":
        print("Ange ett giltigt värde")

    elif user_choice == "h":
        dividend = int(input("Vilket tal ska delas?\n"))
        divisor  = int(input("Med vad ska det delas?\n"))
        print(dividend / divisor)

    else:
        dividend = float(input("Vilket tal ska delas?\n"))
        divisor  = float(input("Med vad ska det delas?\n"))
        print(dividend / divisor)
    print("")