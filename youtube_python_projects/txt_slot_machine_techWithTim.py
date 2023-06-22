"""
# Text Based Slot Machine

README:

## Functions

deposit: takes user input. accepts digits. loops until digit is input.
get_number_of_lines: gets the number of lines the user is betting on. accpets digits. 
                    loops until valid digit is input.
get_bet: takes user imput. accepts bet amounts mutiplied by lines 
        to fit bet allowance, based on deposited money.
"""
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def deposit():
    while True:
        amount = input("Deposit an Amount of Money - $")
        if amount.isdigit():
            amount = int(amount) # convert amount to type int here
            if amount > 0:
                break
            else:
                print("Please enter a valid bet amount: ")
        else:
            print("Please enter a valid bet amount: ")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines) # convert amount to type int here
            if 1 <= lines <= MAX_LINES: #checks if the value is in between two values
                break
            else:
                print("Please enter a valid number: ")
        else:
            print("Please enter a valid number: ")
    return lines

def get_bet():
    while True:
        amount = input("Bet an Amount of Money for Each Line - $")
        if amount.isdigit():
            amount = int(amount) # convert amount to type int here
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a valid bet amount: ")
    return amount

def check_winnings(columns, lines, bet, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
            else:
                winnings += values[symbol] * bet
    return winnings

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count): 
            # the above underscore is an 'anonymous variable', 
            # for counting & not needing to use a real variable
            all_symbols.append(symbol) 
    
    columns = [] #define an empty list named 'columns', that will hold all 3 columns we are about to make

    for _ in range(cols): # this will generate an empty column for each column we need (this loops 3 times)
        current_symbols = all_symbols[:] # a list that gets filled with the right number of symbols from all_symbols
                                        #the '[:]' at the end copies all data from one list to another
        buffer_list = [] # an empty list to hold the symbols we are about to randomly pick
        
        for _ in range(rows): #loop thru the number of values we need to generate (number of rows)
            value = random.choice(current_symbols) # picks a random value from our copid symbol list
            current_symbols.remove(value) # remove the picked value from the list so we dont pick it again 
            buffer_list.append(value) # add the picked value to the current column being generated

        columns.append(buffer_list) #adds the symbol-filled columns from the buffer_list to 'columns' list
    return columns # returns all three columns with symbols into the above 'columns' list

def print_slot_machine(columns): #prints thru each column of our slot machine
    for row in range(len(columns[0])):
        for i, column, in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def main():
    balance = deposit()
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough deposited. You have: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")

"""
runs the code upon call of this file
"""
if __name__ == '__main__':
    main()
