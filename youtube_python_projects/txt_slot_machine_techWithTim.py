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

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count): 
            # the above underscore is an 'anonymous variable', 
            # for counting & not needing to use a real variable
            all_symbols.append(symbol)

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


"""
runs the code upon call of this file
"""
if __name__ == '__main__':
    main()
