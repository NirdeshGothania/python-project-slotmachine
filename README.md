# Slot Machine Game

## Overview
This is a simple console-based slot machine game implemented in Python. The game allows users to simulate playing a slot machine with multiple lines and adjustable bets.

## Files
- `main.py`: The main Python script containing the slot machine game logic.

## How to Run
1. Clone or download the repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the project directory.
4. Run the command: 
    ```
    python main.py
    ```

## Gameplay
1. **Deposit**: Enter the initial amount you want to start the game with.
   - You will be prompted to enter a valid positive amount.
   ```
   Enter the amount: $ 1000
   ```

4. **Play**: Press Enter to play the slot machine.
   - The game will display the results of the spin, including winnings.
   ```
   Press enter to play! (x -> exit)
   ```

2. **Number of Lines**: Choose the number of lines you want to bet on.
   - You can bet on 1 to 5 lines.
   ```
   Enter the number of lines for betting (1-5)? 5
   ```

3. **Bet Amount**: Enter the bet amount for each line.
   - The total bet amount must be between $100 and $10,000,000.
   ```
   Enter the bet amount on each line: 100
   You are betting $100.0 on 5 lines. Total bet is equal to: $500.0
   ```

5. **Exit**: Press 'x' to exit the game at any time.

## Results
- Displayed are the symbols that appear on the slot machine upon spinning.
    ```
    B | E | E | C | E
    E | D | C | B | B
    E | C | E | D | D
    ```
- The output includes the winning amount, the corresponding line numbers where you won, and your updated current balance.
    ```
    You won $0
    You won on lines:
    Your current balance is $500.0
    ```

## Customization
Feel free to modify the `symbols_count` and `symbols_weight` dictionaries in the script to change the symbols and their corresponding weights.


Enjoy the game!
