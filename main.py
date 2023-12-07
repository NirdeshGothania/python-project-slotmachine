import random

MAX_LINES = 5
MAX_BET = 10000000
MIN_BET = 100

WHEEL_COUNT = 3
COLS = 5

symbols_count = {
    "A": 2,
    "B": 3,
    "C": 4,
    "D": 8,
    "E": 10
}

symbols_weight = {
    "A": 8,
    "B": 7,
    "C": 6,
    "D": 2,
    "E": 1
}


def win(columns, lines, bet, values):
    wins = 0
    win_lines = []
    
    if not columns or not columns[0]:
        return wins, win_lines
    
    for line in range(lines):
        symbol = columns[0][line] if line < len(columns[0]) else None
        if symbol is None:
            break
        
        for column in columns:
            check = column[line] if line < len(column) else None
            if symbol != check:
                break
        else:
            wins += values[symbol] * bet
            win_lines.append(line + 1)

    return wins, win_lines

def slotMachinespin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for col in range(cols):
        column = []
        current_sym = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_sym)
            current_sym.remove(value)
            column.append(value)
        
        columns.append(column)
    
    return columns

def printBet(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], "|", end=" ")
            else:
                print(column[row])


def deposit():
    while True:
        amount = input("Enter the amount: $ ")
        if amount.replace(".", "", 1).isdigit():  
            amount = float(amount)
            if amount > 0:
                break
            else:
                print("Please enter a valid amount")
        else:
            print("Please enter a valid amount")

    return amount    

# print(deposit())

def linesCount():
    while True:
        lines = input("Enter the number of lines for betting (1-"+str(MAX_LINES)+")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines")
        else:
            print("Please enter a valid number of lines")
    
    return lines

def eachBet():
    while True:
        bet = input("Enter the bet amount on each line: ")
        if bet.replace(".", "", 1).isdigit():  
            bet = float(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Please enter a valid bet between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a valid bet")

    return bet

def spin(balance):
    lines = linesCount()
    while True:
        bet = eachBet()
        totalBet = bet * lines
        if totalBet <= balance:
            break
        else:
            print("You doesn't have enough balance. Enter a valid bet")

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${totalBet}")
    # print(balance, lines)

    slots = slotMachinespin(WHEEL_COUNT, COLS, symbols_count)
    printBet(slots)
    wins, wining_lines = win(slots, lines, bet, symbols_weight)
    print(f"You won ${wins}")
    print(f"You won on lines:", *wining_lines)

    return wins - totalBet
    
def main():
    balance = deposit()
    while True:
        print(f"Your current balance is ${balance}")
        answer = input("Press enter to play! (x -> exit)")
        if answer == "q":
            break
        
        balance += spin(balance)
    print(f"Remaining balance: ${balance}")




main()