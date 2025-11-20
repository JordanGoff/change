# Practice making change for a customer.

from random import uniform
import os


def clear():
    """Clear the screen."""
    os.system("cls")




def coins(amount):
    """Calculate how many dollars and coins the amount will be."""
    # Initialize the money.
    hundred = 0
    fifty = 0
    twenty = 0
    ten = 0
    five = 0
    one = 0
    quarter = 0
    dime = 0
    nickel = 0
    penny = 0
    
    # Calculate the number of dollars.
    if amount >= 100:
        hundred = int(amount) // 100
        amount = amount - 100 * hundred
    if amount >= 50:
        fifty = int(amount) // 50
        amount = amount - 50 * fifty
    if amount >= 20:
        twenty = int(amount) // 20
        amount = amount - 20 * twenty
    if amount >= 10:
        ten = int(amount) // 10
        amount = amount - 10 * ten
    if amount >= 5:
        five = int(amount) // 5
        amount = amount - 5 * five
    if amount >= 1:
        one = int(amount)
        amount = amount - one
    
    # Calculate the number of coins.
    amount = round(100 * amount)
    if amount >= 25:
        quarter = amount // 25
        amount = amount - 25 * quarter
    if amount >= 10:
        dime = amount // 10
        amount = amount - 10 * dime
    if amount >= 5:
        nickel = amount // 5
        amount = amount - 5 * nickel
    if amount >= 1:
        penny = amount
    
    # Initialize the string.
    string = ""
    
    # Create the dollar and coin string of the value.
    if hundred:
        string = string + f"\nHundred: {hundred}"
    if fifty:
        string = string + f"\nFifty: {fifty}"
    if twenty:
        string = string + f"\nTwenty: {twenty}"
    if ten:
        string = string + f"\nTen: {ten}"
    if five:
        string = string + f"\nFive: {five}"
    if one:
        string = string + f"\nOne: {one}"
    if quarter:
        string = string + f"\nQuarter: {quarter}"
    if dime:
        string = string + f"\nDime: {dime}"
    if nickel:
        string = string + f"\nNickel: {nickel}"
    if penny:
        string = string + f"\nPenny: {penny}"
    
    return string
    

def main():
    """Execute the program."""
    clear()
    start = input("Type q to go back: ")
    clear()
    if start == "q":
        return None

    while True:
        # Choose the minimum number.
        while True:
            a = input("Minimum: ")
            clear()
            if a == "q":
                return None
            try:
                a = float(a)
                a = round(a, 2)
                break
            except:
                continue
        
        # Choose the maximum number.
        while True:
            print(f"Minimum: {a}")
            b = input("Maximum: ")
            clear()
            if b == "q":
                break
            try:
                b = float(b)
                b = round(b, 2)
                break
            except:
                continue
        
        # Go back to the minimum number.
        if b == "q" or a > b:
            continue
        
        # Initialize the loop.
        check = ""
        
        while True:
            total = round(uniform(a, b), 2)
            pay = round(uniform(total, b), 2)
            change = round(pay - total, 2)
            print(f"Pay: ${pay}")
            print(f"Amount: ${total}")
            
            # Check if the user wants to go back.
            check = input()
            if check == "q":
                clear()
                break
            
            value = coins(change)
            print(f"${change}")
            print(value)
            
            # Check if the user wants to go back.
            check = input()
            clear()
            if check == "q":
                break


if __name__ == "__main__":
    main()