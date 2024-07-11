# Casino Slot Machine Game

## Project Title
Casino_Game_By_HH

## Project Goals
The goal of this project is to create an engaging and interactive command-line slot machine game. Players can set their initial balance, place bets, and spin the slot machine to win or lose based on the outcome. This project demonstrates basic Python programming concepts such as conditionals, loops, and user input handling, as well as more advanced features like animations and colored text output.

## Solution
The problem is solved using Python's built-in libraries and simple control structures. The game allows players to set an initial balance, place bets, and choose a multiplier for potential winnings. The slot machine randomly generates three emojis for each spin and determines the outcome based on predefined rules. The following technologies and libraries are used:

- Python 3
- `random` library for generating random emojis
- `time` library for creating the spin animation
- `os` library for clearing the console screen

## Features
- Initial balance setting
- Bet placing
- Multiplier selection
- Animated slot machine spins
- Colored and formatted console output
- Emoji-based outcomes with special rewards

## Source Code
Use this link to go directly to the source code: [Source Code](Casino_Game_By_HH.py)

## Live Demo
You can play the game directly in your Web browser here:
[TRY IT NOW!](https://replit.com/join/ngflwomuog-hhristov2007)

Alternatively, you can run the game on your local machine by following these steps:

1. Download the source code from the provided link.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the source code file.
4. Run the game by executing the following command:
    ```sh
    python Casino_Slot_Machine_By_HH.py
    ```

## Inputs and Outputs
### Inputs
- The user is prompted to enter their initial balance.
- The user chooses a bet amount for each spin.
- The user selects a multiplier (1 or 2).

### Outputs
- The game displays the user's current balance.
- Animated slot machine spins showing randomly chosen emojis.
- The game announces the outcome of each spin (win, loss, or no change).
- Special rewards for certain emoji combinations (e.g., JACKPOT).

## Rules
1. Enter your initial balance.
2. Choose a bet amount for each spin.
3. Choose a multiplier (1 or 2):
   - Multiplier 1: You win, lose, or stay with your bet amount.
   - Multiplier 2: If you win, you get double your bet as a reward. If you lose, you lose double your bet amount.
4. Special rewards if you get three consecutive emojis from these (🍬, 💰, ✨):
   - Three 🍬: Your bet multiplied by 5.
   - Three 💰: Your bet multiplied by 10.
   - Three ✨: JACKPOT of 2500 $!
5. If you get two matching emojis, you keep your balance and don't lose anything.
6. If you get only one emoji, you lose your bet.

## Color Codes
The game uses colored text to enhance the user experience. Here are the color codes used:
- **Green**: Game rules and winning messages.
- **Orange**: Slot machine spin messages.
- **Yellow**: Messages for returning the bet.
- **Red**: Losing messages.
- **Cyan**: Good luck message.

## Example Run
```sh
Enter your initial balance: 100.00
Your current balance is: 100.00 $
Enter your bet: 10
Choose a multiplier (1 or 2): 2
Spinning the slot machine...
🍒 | 🍋 | 🍒
You got your bet back: 20.00 $
Your current balance is: 100.00 $
Do you want to play again? (yes/no): no
Your final balance is: 100.00 $. Thank you for playing!
```

## Contribution
This project is a great starting point for beginners to understand basic and intermediate programming concepts in Python. Contributions are welcome! Feel free to fork the repository and submit pull requests to add more features or improvements.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Have fun playing the game and feel free to modify the code to add more features or improvements!
